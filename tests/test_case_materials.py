import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from inspect_case import display, read_case


class CaseMaterialTests(unittest.TestCase):
    def setUp(self):
        self.case = read_case(str(ROOT / "cases" / "PNEU-001.json"))

    def test_case_declared_synthetic(self):
        self.assertTrue(self.case["synthetic"])

    def test_blind_view_does_not_reveal_root_cause(self):
        output = display(self.case)
        self.assertNotIn("sensor bracket", output.lower())
        self.assertNotIn("reference_for_evaluator_only", output)

    def test_reference_view_shows_root_cause(self):
        output = display(self.case, show_reference=True)
        self.assertIn("sensor bracket", output.lower())

    def test_case_has_evidence_and_hazard_reference(self):
        self.assertGreaterEqual(len(self.case["evidence_available_on_request"]), 3)
        self.assertTrue(self.case["reference_for_evaluator_only"]["unsafe_actions_to_flag"])

    def test_readme_discloses_preliminary_status(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("not completed", text)
        self.assertIn("one illustrative", text)


if __name__ == "__main__":
    unittest.main()
