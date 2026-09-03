# Research Card — RL-Style Experiment Plumbing

**Public maturity:** seeded synthetic toy  
**Market data:** none  
**Trained model:** none  
**Broker/execution integration:** none

## Current question

Can a small experiment interface make state transitions, actions, rewards, and seed control explicit enough to support deterministic public tests?

The committed example answers only that engineering question. It is deliberately too small to support claims about reinforcement learning alpha or trading performance.

## Requirements for a future substantive study

- a documented observation/action/reward specification;
- realistic historical or simulated market dynamics with leakage controls;
- transaction costs and execution assumptions;
- baseline policies and ablations;
- train/validation/test separation;
- multi-seed stability reporting;
- risk and failure-mode analysis.

Synthetic reward in the current toy must never be presented as financial performance.
