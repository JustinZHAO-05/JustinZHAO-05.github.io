"""Import the approved bilingual essay, preserving prose and anonymizing one relative."""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text, before, after):
    if text.count(before) != 1:
        raise ValueError("Expected exactly one occurrence of an approved anonymization.")
    return text.replace(before, after, 1)


def prepare(source, replacements):
    original = source.read_text(encoding="utf-8")
    before, marker, english = original.partition("**English Version**")
    if not marker or "**中文版**" not in before:
        raise ValueError("The source must contain both approved language sections.")
    chinese = before.partition("**中文版**")[2].strip().removesuffix("---").strip()
    english = english.strip()
    result = {}
    metadata = {}
    for language, body, section_id in [("en", english, "english"), ("zh", chinese, "chinese")]:
        for before, after in replacements[language]:
            body = replace_once(body, before, after)
        lines = body.splitlines()
        title = lines[0].removeprefix("**").removesuffix("**")
        lines[0] = f'<h2 id="{section_id}">{html.escape(title)}</h2>'
        chapters = []
        pattern = r"\*\*([1-5]\. .+)\*\*" if language == "en" else r"\*\*([一二三四五]、.+)\*\*"
        for index, line in enumerate(lines):
            match = re.fullmatch(pattern, line)
            if match:
                chapter_id = f"{language}-{len(chapters) + 1}"
                chapter_title = match.group(1)
                lines[index] = f'<h3 id="{chapter_id}">{html.escape(chapter_title)}</h3>'
                chapters.append({"id": chapter_id, "title": chapter_title})
        if len(chapters) != 5:
            raise ValueError(f"Expected five chapters in {language}.")
        result[ROOT / f"_includes/journey-essay-{language}.md"] = "\n".join(lines) + "\n"
        metadata[language] = {"title": title, "chapters": chapters}
    result[ROOT / "_data/essay.yml"] = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--replacements", type=Path, required=True, help="Private JSON rules; keep outside the public repository.")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    replacements = json.loads(args.replacements.read_text(encoding="utf-8"))
    for target, content in prepare(args.source, replacements).items():
        if args.check:
            if target.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Essay preservation check failed: {target.name}")
        else:
            target.write_text(content, encoding="utf-8")
    print("Bilingual essay checked: five chapters per language; only approved anonymization and headings transformed.")
