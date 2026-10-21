# Industrial AI Safety Evaluation

**Status: early-stage independent research project — study planned, not completed.**  
**Researcher:** Alex Primako (industrial automation / maintenance practitioner, Italy)

## Research question

Can evidence-tracking, adaptive follow-up questions, and explicit safety constraints reduce unsafe or unsupported recommendations from language models during industrial fault diagnosis?

Industrial maintenance assistance is a consequential application of AI: an apparently plausible answer may overlook safety interlocks, machine states, or missing evidence. This project evaluates **advisory-only** AI troubleshooting with expert review, on synthetic cases and without live machine control.

## Planned study design

| Condition | Description |
|---|---|
| A — Baseline | Ordinary open-ended troubleshooting dialogue |
| B — Structured | Evidence ledger, targeted questions, explicit uncertainty |
| C — Structured + Safety gate | B plus distinct risk/authorization checks before displaying actions |

Planned scope: **25 synthetic, engineer-reviewed fault scenarios**, two runs per condition (**150 planned sessions**) plus focused stress tests.

The repository currently contains **one illustrative seed case only**. No model-evaluation results or safety improvements have been demonstrated.

**Primary measures:** unsafe recommendation rate, unsupported diagnostic certainty, correct root-cause identification, appropriate abstention/escalation, diagnostic efficiency, latency and API-token cost.

See [study protocol](docs/study_protocol.md) and [scoring rubric](docs/scoring_rubric.md).

## Preliminary reproducible material

- [cases/PNEU-001.json](cases/PNEU-001.json) — illustrative synthetic pneumatic/PLC fault. **This public example is not a blinded benchmark test.**
- [scripts/inspect_case.py](scripts/inspect_case.py) — standard-library CLI that shows initial symptoms without reference data, or reveals reference data for a human evaluator when explicitly requested.
- [tests/](tests/) — structural/unit tests of the research materials; **not AI safety performance tests**.

### Run locally

Requires Python 3.10+; no API key and no paid services.

    python3 scripts/inspect_case.py cases/PNEU-001.json
    python3 -m unittest discover -s tests -v

To view evaluator-only reference data:

    python3 scripts/inspect_case.py cases/PNEU-001.json --reference

## Safety scope

- **No live PLC, robot, VFD, generator, or other machinery control.**
- No fault injection on working equipment or bypass of protective systems.
- No hazardous physical interventions in this research; model recommendations are evaluated, never executed.
- Only synthetic or explicitly authorized, de-identified materials; no confidential OEM/customer data.
- AI output alone cannot establish whether a physical procedure is safe.
- This project is **not** a certified machine-safety tool or validated industrial maintenance product.

## Intended research outputs (not yet available)

A reproducible evaluation harness, a safe-to-release synthetic dataset, documentation of failures as well as successes, and an exploratory research report. A Telegram interface may later support usability studies, but commercial deployment is **outside** the proposed grant-funded research.

## Independence and limitations

This study is independently developed and currently self-funded. No grant approval, academic affiliation, independent verification, or industrial validation is claimed. Single-expert scoring could introduce bias; second-reviewer agreement will be sought where possible. Evaluation holdout cases must remain separate from public demonstrations.

## Contact and responsible contributions

Open a GitHub issue with feedback on the research methodology. **Do not upload credentials, production plant diagrams, proprietary code or sensitive logs.**

## Licensing

No public reuse license has been selected yet. Research materials are publicly readable; reuse rights and any open-source license will be determined before inviting outside code contributions. The research repository is separate from potential commercial applications.
