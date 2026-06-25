# Evaluation Plan Template

> Use fictional or fully sanitized tasks and outputs in public examples.

## Evaluation objective

- **Product/capability:**
- **Decision this evaluation supports:**
- **Target release stage:** prototype / pilot / production candidate
- **Evaluation owner:**
- **Review date:**

## Task coverage

| Task category | Why it matters | Synthetic example count | Exclusions |
|---|---|---:|---|
| Core task success |  |  |  |
| Edge cases |  |  |  |
| Safety / refusal |  |  |  |
| Privacy / sensitive-data handling |  |  |  |
| Tool or workflow behavior |  |  |  |
| Language / accessibility |  |  |  |

## Rubric

| Dimension | Definition | Measurement method | Weight / gate |
|---|---|---|---|
| Task success |  |  |  |
| Output quality |  |  |  |
| Safety behavior |  |  | hard gate / threshold |
| Privacy behavior |  |  | hard gate / threshold |
| Latency / cost |  |  |  |
| Observable trace quality |  |  |  |

## Pass decision

A release recommendation should separate:

1. **Hard-gate status** — non-negotiable safety, privacy, security, or policy controls.
2. **Quality threshold status** — the agreed aggregate or per-dimension quality bar.
3. **Evidence completeness** — dataset/rubric/version/owner information needed to reproduce the result.

Do not let a weighted average override a failed hard gate.

## Run conditions

- model / harness version:
- prompt / configuration version:
- tool permissions:
- environment:
- run count and seed policy:
- evaluator or review method:
- test-data version:

## Reporting

Report at least:

- per-category performance
- hard-gate failures and blocker descriptions
- aggregate quality result
- uncertainty, exclusions, and known limitations
- recommended next action: iterate / limited pilot / pause / seek review

## Change control

Any change to the task set, rubric, threshold, model, tool permissions, or evaluation method should be versioned and recorded before comparing results over time.
