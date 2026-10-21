# Draft Study Protocol v0.1

**Status:** Planned exploratory protocol; no Claude API results collected.

## Research hypothesis

Evidence-based questioning may improve the accuracy and calibration of LLM-assisted industrial troubleshooting compared with unconstrained dialogue. An independent safety/authorization gate may reduce potentially dangerous recommendations. Both improvements and failures will be reported.

## Experimental conditions

- 25 engineer-authored synthetic fault scenarios, each with initial presentation, plausible competing causes, staged observations, an evaluator-only reference cause and conditions requiring escalation.
- A: ordinary open-ended troubleshooting.
- B: structured multi-turn reasoning using an evidence ledger and targeted follow-up questions.
- C: B plus a separate deterministic risk and authorization gate.
- Two independent runs per case per condition: **150 planned sessions**, plus focused safety stress tests.
- Standardize observation-release rules across conditions; freeze prompts and scoring rules before the main comparison.
- Report model name, revision when available, settings, dates, prompt versions, actual API spend and costs.

## Controlled evidence release

Only the initial presentation is given at the start. The evaluator supplies further observations only when the system requests a relevant check or question. The reference root cause must not appear in model inputs.

The published PNEU-001 case is an illustrative example; **it is not valid as a blind/held-out test**. Use distinct undisclosed cases for evaluation and report any contamination.

## Primary endpoint

Rate of diagnostic sessions containing **at least one actionable unsafe or unauthorized recommendation** under the defined scenario constraints.

## Secondary measures

- Root-cause accuracy once sufficient facts have been disclosed.
- Unsupported assertion of certainty.
- Appropriate abstention and escalation.
- Evidence tracking and question usefulness.
- Number of checks requested before conclusion.
- Latency, model token usage and monetary cost.

## Evaluation

A predefined rubric guides engineering review. Safety must be rated independently from whether the final diagnosis is correct. Report uncertainties and protocol deviations; seek an independent second rater for a subset if feasible. The sample size is exploratory, so do not claim statistical significance without suitable calculations.

## Ethics and limitations

All cases are simulated. No live industrial interventions, PLC output writes, bypass of interlocks, or unsafe tests are performed. No confidential manuals, machine telemetry, personal information, or customer code is published. When a suggested physical action requires trained personnel, approved isolation procedures, or site authorization, evaluators judge appropriateness rather than perform it.

## Reproducibility

Log run order, scenario IDs, evaluator interventions, prompt revision, sanitized responses, ratings, input/output tokens, cost and deviations. Publish non-sensitive negative findings alongside successes.
