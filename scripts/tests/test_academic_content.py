"""Regression checks for the shared website and academic CV records."""
import importlib.util
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("academic", ROOT / "scripts/build_academic_content.py")
ACADEMIC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ACADEMIC)


class AcademicContentTests(unittest.TestCase):
    def setUp(self):
        self.profile = ACADEMIC.read(ROOT / "_data/profile.yml")
        self.experience = ACADEMIC.read(ROOT / "_data/experience.yml")
        self.projects = ACADEMIC.read(ROOT / "_data/projects.yml")
        self.courses = ACADEMIC.read(ROOT / "_data/courses.yml")
        self.studies = ACADEMIC.read(ROOT / "_data/independent_study.yml")
        self.reading = ACADEMIC.read(ROOT / "_data/reading.yml")

    def cv(self, full=False):
        return ACADEMIC.render_cv(self.profile, self.experience, self.projects, self.courses, ACADEMIC.publication_records(), self.studies, self.reading, full)

    def test_grades_and_scopes(self):
        self.assertEqual(len(self.courses), 22)
        self.assertEqual(sum(c.get("grade") is not None for c in self.courses), 18)
        grades = {x["title"]: x.get("grade") for x in self.courses}
        self.assertEqual(grades["Digital Circuits"], 96)
        self.assertEqual(grades["Theory of Motor"], 98)
        self.assertEqual(grades["Intelligent Medical Signal Processing"], 89)
        self.assertIn(r"Digital Circuits \textbf{96}", self.cv())
        self.assertIn(r"Theory of Motor \textbf{98}", self.cv())
        self.assertNotIn(r"Intelligent Medical Signal Processing \textbf{89}", self.cv())
        self.assertIn(r"Intelligent Medical Signal Processing \textbf{89}", self.cv(True))

    def test_four_books_and_printable_contacts_in_both_cvs(self):
        for full in (False, True):
            cv = self.cv(full)
            for book in self.reading:
                self.assertIn(ACADEMIC.tex(book["short_title"] if not full else book["title"]), cv)
            for value in ["justinzhao-05.github.io", "github.com/JustinZHAO-05", "0009-0003-5342-6611", "/intellectual-journey/"]:
                self.assertIn(value, cv)
            self.assertIn("CASE Summer School" if not full else "(CASE)", cv)
            self.assertIn("95.70/100", cv)

    def test_selected_projects_and_certified_study(self):
        main = self.cv()
        for project in ["Nonholonomic Dead-End Escape", "Eight-Cable-Driven"]:
            self.assertIn(project, main)
        for project in ["MNIST MLP", "SAGIN ML", "VeriRotate", "Q-RIS-UAV"]:
            self.assertNotIn(project, main)
        self.assertEqual(len(self.studies), 4)
        for text in [main, self.cv(True), str(self.studies)]:
            self.assertNotIn("Stanford", text)
            self.assertNotIn("University of Washington", text)

    def test_essay_chapters_and_anonymization(self):
        metadata = ACADEMIC.read(ROOT / "_data/essay.yml")
        for language in ("en", "zh"):
            body = (ROOT / f"_includes/journey-essay-{language}.md").read_text(encoding="utf-8")
            self.assertEqual(len(metadata[language]["chapters"]), 5)
            self.assertEqual(body.count('<h3 id="'), 5)
        self.assertIn("a close relative", (ROOT / "_includes/journey-essay-en.md").read_text(encoding="utf-8"))
        self.assertIn("我的一位亲人", (ROOT / "_includes/journey-essay-zh.md").read_text(encoding="utf-8"))

    def test_timeline_links_have_no_empty_values(self):
        journey = yaml.safe_load((ROOT / "_data/journey.yml").read_text(encoding="utf-8"))
        self.assertEqual(len(journey), 7)
        for node in journey:
            self.assertTrue(node["dates"])
            self.assertTrue(node["summary"])
            for link in node["links"]:
                self.assertTrue(link["url"])
                self.assertTrue(link["label"])


if __name__ == "__main__":
    unittest.main()
