#!/usr/bin/env python3
"""Offline educational helper: shows only initial observations by default."""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def read_case(filename: str) -> dict:
    case = json.loads(Path(filename).read_text(encoding="utf-8"))
    required = {"case_id", "initial_presentation", "evidence_available_on_request", "reference_for_evaluator_only"}
    missing = required - set(case)
    if missing:
        raise ValueError(f"Missing required case keys: {sorted(missing)}")
    return case


def display(case: dict, show_reference: bool = False) -> str:
    out = [f"CASE: {case['case_id']}", "INITIAL PRESENTATION:", case["initial_presentation"]]
    if show_reference:
        out.extend(["", "EVIDENCE (EVALUATOR ONLY):"])
        for item in case["evidence_available_on_request"]:
            out.append(f"- {item['topic']}: {item['observation']}")
        out.extend(["", "REFERENCE (EVALUATOR ONLY):",
                    json.dumps(case["reference_for_evaluator_only"], indent=2, ensure_ascii=False)])
    else:
        out.append("\nReference observations and ground truth withheld. Use --reference for evaluator review.")
    return "\n".join(out)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("case_file", type=str)
    p.add_argument("--reference", action="store_true", help="Reveal evaluator-only reference data")
    args = p.parse_args()
    print(display(read_case(args.case_file), show_reference=args.reference))
