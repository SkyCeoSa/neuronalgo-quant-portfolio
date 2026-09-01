# Public Research Projects

Every project in this directory is intentionally scoped below production trading software. The labels below describe the evidence that is actually committed.

| Project | Current public evidence | Reproducibility |
| --- | --- | --- |
| [`core/stat_arb_1`](core/stat_arb_1/) | Deterministic price-to-return metrics demo | Base CI / offline |
| [`smc-backtester`](smc-backtester/) | Deterministic return-series metrics demo plus SMC design notes | Base CI / offline |
| [`rl-research-platform`](rl-research-platform/) | Seeded toy environment and deterministic policy loop | Base CI / offline |
| [`qlib-ml-pipeline`](qlib-ml-pipeline/) | Output-free exploratory Qlib notebook and methodology notes | Optional; requires separately configured local Qlib data |
| [`open-source-customizations`](open-source-customizations/) | Design notes for possible public integrations | Documentation only |

A project name is not a validation claim. In particular, the current `stat_arb_1` and `smc-backtester` examples demonstrate deterministic metrics plumbing; they do not contain complete implementations of the named trading approaches.

No project here connects to a broker, manages a portfolio, contains live account data, or guarantees future returns.
