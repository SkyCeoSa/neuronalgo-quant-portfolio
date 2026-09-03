"""Seeded toy environment for deterministic public research smoke tests."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from typing import Sequence

import numpy as np


@dataclass
class DummyEnv:
    """Small synthetic environment with an owned deterministic random generator."""

    seed: int = 7
    window: int = 32
    n_features: int = 8
    _rng: np.random.Generator = field(init=False, repr=False)
    _state: np.ndarray = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._rng = np.random.default_rng(self.seed)
        self._state = np.zeros((self.window, self.n_features), dtype=float)
        self.reset(self.seed)

    def reset(self, seed: int | None = None) -> np.ndarray:
        if seed is not None:
            self.seed = seed
            self._rng = np.random.default_rng(seed)
        self._state = self._rng.normal(0.0, 1.0, size=(self.window, self.n_features))
        return self._state.copy()

    def step(self, action: int) -> tuple[np.ndarray, float]:
        if action not in (-1, 0, 1):
            raise ValueError("action must be -1, 0, or 1")

        signal = float(np.tanh(self._state[-1, 0]))
        reward_noise = float(self._rng.normal(0.0, 0.0001))
        reward = float(action * signal * 0.001 + reward_noise)
        next_row = self._rng.normal(0.0, 1.0, size=self.n_features)
        self._state = np.vstack((self._state[1:], next_row))
        return self._state.copy(), reward


def deterministic_policy(observation: np.ndarray) -> int:
    """Map the latest first feature to a simple discrete action."""
    signal = float(observation[-1, 0])
    if signal > 0.25:
        return 1
    if signal < -0.25:
        return -1
    return 0


def run_episode(seed: int = 7, steps: int = 50) -> dict[str, float | int]:
    if steps <= 0:
        raise ValueError("steps must be positive")

    env = DummyEnv(seed=seed)
    observation = env.reset(seed)
    total_reward = 0.0
    nonzero_actions = 0

    for _ in range(steps):
        action = deterministic_policy(observation)
        nonzero_actions += int(action != 0)
        observation, reward = env.step(action)
        total_reward += reward

    return {
        "seed": seed,
        "steps": steps,
        "nonzero_actions": nonzero_actions,
        "synthetic_total_reward": total_reward,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--steps", type=int, default=50)
    args = parser.parse_args(argv)
    print(json.dumps(run_episode(seed=args.seed, steps=args.steps), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
