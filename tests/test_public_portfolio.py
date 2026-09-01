"""Deterministic public-portfolio contract and smoke tests."""

from __future__ import annotations

import importlib.util
import json
import math
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


STAT_ARB = load_module("public_stat_arb_demo", "projects/core/stat_arb_1/backtest.py")
SMC = load_module("public_smc_demo", "projects/smc-backtester/backtest.py")
RL = load_module("public_rl_demo", "projects/rl-research-platform/example_agent.py")


class DeterministicDemoTests(unittest.TestCase):
    def test_stat_arb_fixture_is_deterministic(self) -> None:
        fixture = ROOT / "projects/core/stat_arb_1/sample_data.csv"
        first = STAT_ARB.load_returns(fixture)
        second = STAT_ARB.load_returns(fixture)
        np.testing.assert_array_equal(first, second)
        self.assertGreaterEqual(first.size, 2)
        metrics = STAT_ARB.compute_metrics(first)
        self.assertEqual(first.size, metrics["n"])
        self.assertTrue(all(math.isfinite(float(value)) for value in metrics.values()))

    def test_smc_fixture_is_deterministic(self) -> None:
        fixture = ROOT / "projects/smc-backtester/sample_data.csv"
        first = SMC.load_returns(fixture)
        second = SMC.load_returns(fixture)
        np.testing.assert_array_equal(first, second)
        self.assertGreaterEqual(first.size, 2)
        metrics = SMC.compute_metrics(first)
        self.assertEqual(first.size, metrics["n"])
        self.assertTrue(all(math.isfinite(float(value)) for value in metrics.values()))

    def test_known_metrics_shape(self) -> None:
        values = np.array([0.01, -0.005, 0.002], dtype=float)
        metrics = STAT_ARB.compute_metrics(values)
        self.assertEqual(3, metrics["n"])
        self.assertAlmostEqual(2.0 / 3.0, metrics["hit_rate"])
        self.assertAlmostEqual(-0.005, metrics["max_drawdown"])

    def test_missing_fixture_fails_instead_of_generating_random_data(self) -> None:
        with self.assertRaises(FileNotFoundError):
            STAT_ARB.load_returns(ROOT / "does-not-exist.csv")
        with self.assertRaises(FileNotFoundError):
            SMC.load_returns(ROOT / "does-not-exist.csv")

    def test_rl_episode_is_seed_reproducible(self) -> None:
        first = RL.run_episode(seed=11, steps=12)
        second = RL.run_episode(seed=11, steps=12)
        self.assertEqual(first, second)
        self.assertNotEqual(first, RL.run_episode(seed=12, steps=12))

    def test_explicit_output_goes_only_to_requested_directory(self) -> None:
        fixture = ROOT / "projects/core/stat_arb_1/sample_data.csv"
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "derived"
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "projects/core/stat_arb_1/backtest.py"),
                    "--input",
                    str(fixture),
                    "--output-dir",
                    str(destination),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn('"n"', result.stdout)
            self.assertTrue((destination / "metrics.json").is_file())
            self.assertTrue((destination / "daily_returns.csv").is_file())
        self.assertFalse((ROOT / "projects/core/stat_arb_1/outputs").exists())


class PublicContentTests(unittest.TestCase):
    PLACEHOLDERS = (
        "__REPLACE_ME__",
        "__REPLACE_ME_USERNAME__",
        "founder@__REPLACE_ME__",
        "Copy code",
    )
    UNSUPPORTED_PHRASES = (
        "production-ready",
        "ready for deployment",
        "investable",
    )
    SECRET_ASSIGNMENT = re.compile(
        r"(?i)(api[_-]?key|password|secret|token)\s*[:=]\s*['\"][^'\"]+['\"]"
    )
    MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

    @classmethod
    def public_text_files(cls) -> list[Path]:
        files: list[Path] = []
        for pattern in ("*.md", "*.py", "*.sh", "*.toml", "*.yml", "*.yaml", "*.ipynb"):
            files.extend(ROOT.rglob(pattern))
        return [path for path in files if ".git" not in path.parts and ".venv" not in path.parts]

    def test_no_scaffold_placeholders_or_unsupported_claims(self) -> None:
        for path in self.public_text_files():
            if path.is_relative_to(ROOT / "tests"):
                continue
            text = path.read_text(encoding="utf-8")
            for marker in self.PLACEHOLDERS:
                self.assertNotIn(marker, text, f"placeholder in {path.relative_to(ROOT)}")
            lowered = text.lower()
            for phrase in self.UNSUPPORTED_PHRASES:
                self.assertNotIn(phrase, lowered, f"unsupported claim in {path.relative_to(ROOT)}")

    def test_no_obvious_hard_coded_secret_assignments(self) -> None:
        for path in self.public_text_files():
            if path.is_relative_to(ROOT / "tests"):
                continue
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(
                self.SECRET_ASSIGNMENT.search(text),
                f"possible hard-coded secret in {path.relative_to(ROOT)}",
            )

    def test_markdown_relative_links_resolve(self) -> None:
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts or ".venv" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            for target in self.MARKDOWN_LINK.findall(text):
                target = target.strip().split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = (path.parent / target).resolve()
                self.assertTrue(resolved.exists(), f"broken link {target!r} in {path.relative_to(ROOT)}")

    def test_markdown_fenced_code_blocks_are_balanced(self) -> None:
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts or ".venv" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            fence_lines = sum(1 for line in text.splitlines() if line.lstrip().startswith("```"))
            self.assertEqual(
                0,
                fence_lines % 2,
                f"unbalanced fenced code block in {path.relative_to(ROOT)}",
            )

    def test_readme_contains_required_public_links_and_boundaries(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for url in (
            "https://neuronalgo.com/",
            "https://neuronalgo.com/proof/",
            "https://www.linkedin.com/in/massah",
        ):
            self.assertIn(url, readme)
        self.assertIn("does not guarantee profit", readme)
        self.assertIn("No production trading system is published", readme)

    def test_notebook_is_small_output_free_and_valid_json(self) -> None:
        notebook_path = ROOT / "projects/qlib-ml-pipeline/notebooks/QLIB_NA_WORKFLOW.ipynb"
        self.assertLess(notebook_path.stat().st_size, 100_000)
        notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        self.assertEqual(4, notebook["nbformat"])
        code_cells = [cell for cell in notebook["cells"] if cell.get("cell_type") == "code"]
        self.assertGreaterEqual(len(code_cells), 1)
        for cell in code_cells:
            self.assertIsNone(cell.get("execution_count"))
            self.assertEqual([], cell.get("outputs"))

    def test_base_smoke_paths_have_no_generated_output_directories(self) -> None:
        self.assertFalse((ROOT / "projects/core/stat_arb_1/outputs").exists())
        self.assertFalse((ROOT / "projects/smc-backtester/outputs").exists())


if __name__ == "__main__":
    unittest.main()
