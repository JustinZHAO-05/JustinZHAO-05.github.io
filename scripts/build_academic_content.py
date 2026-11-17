"""Generate TeX bodies, JSON CV and project routes from shared academic records."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def tex(value):
    table = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(table.get(c, c) for c in str(value))


def link(url, label):
    return r"\href{" + url + "}{" + tex(label) + "}"


def section(title):
    return r"\section{" + tex(title) + "}\n"


def entry(title, dates="", institution="", text=""):
    return (r"\cvheading{" + tex(title) + "}{" + tex(dates) + "}\n"
            + (r"\textit{" + tex(institution) + "}\\par\n" if institution else "")
            + (tex(text) + "\\par\n" if text else ""))


def bullets(items):
    return "\\begin{itemize}\n" + "\n".join(r"\item " + tex(x) for x in items) + "\n\\end{itemize}\n"


def publication_records():
    records = []
    for path in sorted((ROOT / "_publications").glob("*.md"), reverse=True):
        data = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
        data.setdefault("year", str(data["date"])[:4])
        records.append(data)
    return records


def render_cv(p, experience, projects, courses, pubs, full):
    e = p["education"]
    lab = next(x for x in experience if x["id"] == "qin-lab")
    nma = next(x for x in experience if x["id"] == "neuromatch")
    imperial = next(x for x in experience if x["id"] == "imperial-research")
    out = (r"\cvheader{" + tex(p["name"]) + "}{" + tex(p["fields"]) + "}{" + tex(p["secondary_field"]) + "}{" + tex(p["email"]) + "}\n")
    out += r"\contactline{" + " / ".join(link(p[k], label) for k, label in [("website", "Website"), ("github", "GitHub"), ("orcid", "ORCID")]) + "}\n"
    out += section("Research Interests") + tex(p["interests"]) + "\\par\n"
    out += section("Education") + entry(e["institution"], e["dates"], e["degree"] + ", " + e["school"])
    out += tex(e["track"] + ". " + e["short_description"]) + "\\par\n"
    out += "\\begin{tabularx}{\\linewidth}{@{}lXX@{}}\n"
    out += r" & \textbf{Overall} & \textbf{Year 3 (Automation)} \\" + "\n"
    for label, key in [("Rank", "rank"), ("Weighted average", "average"), ("GPA", "gpa")]:
        overall = e["overall"][key] + (", " + e["overall"]["percentile"] if key == "rank" else "")
        out += tex(label) + " & " + tex(overall) + " & " + tex(e["year3"][key]) + r" \\" + "\n"
    out += "\\end{tabularx}\n" + section("Research Experience")
    out += entry(lab["title"], lab["dates"], lab["institution"]) + bullets(lab["bullets"])
    out += entry(imperial["title"], imperial["dates"], imperial["institution"], imperial["summary"])
    out += section("Publications and Preprints")
    for kind, title in [("preprint", "Preprints and manuscripts under review"), ("published", "Peer-reviewed publication")]:
        out += r"\pubgroup{" + title + "}\n"
        for pub in pubs:
            if pub.get("kind", "published") != kind:
                continue
            authors = tex(pub["authors"]).replace("Yanzhe Zhao", r"\textbf{Yanzhe Zhao}")
            out += r"\needspace{4\baselineskip}" + "\n" + authors + ". " + link(pub.get("paperurl", pub["doiurl"]), pub["title"]) + ". " + tex(pub["year"]) + ". "
            out += (r"\textit{" + tex(pub["status"]) + "}." if kind == "preprint" else "CSAI 2025, ACM, pp. 126-131. " + link(pub["doiurl"], "DOI"))
            if pub.get("contribution") and (full or kind == "preprint"):
                out += r"\newline " + tex("Contribution: " + pub["contribution"])
            out += "\\par\\smallskip\n"
    if not full:
        out += "\\newpage\n"
    out += section("Research and Project Portfolio" if full else "Selected Research and Projects")
    selected = projects if full else [x for x in projects if x["id"] == "temporal-persistence"]
    for project in selected:
        out += entry(project["title"], "2026" if project.get("featured") else "", project.get("subtitle", project["category"]))
        text = project.get("results", project["summary"]) if full else "Compared latent-state models using run-level cross-validation on 83,210 perceptual judgments from 12 participants."
        out += tex(project["role"] + " " + text) + " " + link(project["links"]["github"], "Code")
        for key, label in [("paper", "Paper"), ("video", "Presentation")]:
            if project["links"].get(key):
                out += " / " + link(project["links"][key], label)
        out += ".\\par\n"
        if full:
            out += tex("Methods: " + project["methods"]) + "\\par\n"
    if not full:
        out += entry(p["neural_project"]["title"], text=p["neural_project"]["summary"]) + link(p["neural_project"]["url"], "Code and reports") + "\\par\n"
        for project in projects:
            if project.get("main_cv"):
                out += entry(project["title"], text=project["role"] + " " + project["summary"]) + link(project["links"]["github"], "Code and documentation") + "\\par\n"
    out += section("Research Training") + entry("Computational Neuroscience", "Jul 2026", "Neuromatch Academy", nma["summary"])
    out += link(nma["certificate"], "Certificate") + "\\par\n"
    if full:
        out += section("Earlier Academic Training")
        for exp in experience:
            if exp["kind"] == "earlier":
                out += entry(exp["title"], exp["dates"], exp["institution"], exp["summary"])
    out += section("Selected Coursework")
    for group in dict.fromkeys(c["cluster"] for c in courses):
        if group == "Additional Engineering Coursework" and not full:
            continue
        values = [tex(c["title"]) + (r" \textbf{" + str(c["grade"]) + "}" if c.get("grade") is not None else "") for c in courses if c["cluster"] == group]
        out += r"\coursegroup{" + tex(group) + "}{" + "; ".join(values) + ".}\n"
    out += section("Skills and Languages")
    for skill in p["skills"]:
        out += r"\skillrow{" + tex(skill["title"]) + "}{" + tex(skill["text"]) + "}\n"
    return out + r"\skillrow{Languages}{Chinese (native); English: " + tex(p["ielts"]) + ".}\n"


def build(cv_dir):
    p = read(ROOT / "_data/profile.yml")
    experience = read(ROOT / "_data/experience.yml")
    courses = read(ROOT / "_data/courses.yml")
    projects = sorted(read(ROOT / "_data/projects.yml"), key=lambda x: x["priority"])
    pubs = publication_records()
    generated = cv_dir / "generated"
    generated.mkdir(parents=True, exist_ok=True)
    for variant in ("main", "full"):
        (generated / f"{variant}.tex").write_text(render_cv(p, experience, projects, courses, pubs, variant == "full"), encoding="utf-8")
    detail_dir = ROOT / "_pages/research"
    detail_dir.mkdir(parents=True, exist_ok=True)
    for project in projects:
        route = project.get("detail", "/projects/" + project["id"].lower() + "/")
        metadata = {"layout": "research", "title": project["title"], "permalink": route, "project_id": project["id"], "author_profile": False}
        (detail_dir / (project["id"].lower() + ".md")).write_text("---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n", encoding="utf-8")
    e = p["education"]
    cv = {
        "basics": {"name": p["name"], "label": p["fields"] + " | " + p["secondary_field"], "image": p["website"].rstrip("/") + p["portrait"], "email": p["email"], "url": p["website"], "summary": p["intro"] + " " + p["interests"], "profiles": [{"network": "GitHub", "url": p["github"]}, {"network": "ORCID", "url": p["orcid"]}]},
        "education": [{"institution": e["institution"], "area": "Automation", "studyType": "B.Eng.", "startDate": e["start"], "endDate": e["graduation"], "gpa": e["overall"]["gpa"], "courses": [c["title"] + (": " + str(c["grade"]) if c.get("grade") is not None else "") for c in courses], "summary": "Overall: " + ", ".join(e["overall"].values()) + "; Year 3: " + ", ".join(e["year3"].values())}],
        "work": [{"name": x["institution"], "position": x["title"], "startDate": x.get("start", ""), "endDate": x.get("end", ""), "summary": x["summary"], "highlights": x.get("bullets", [])} for x in experience if x["kind"] == "research"],
        "certificates": [{"name": "Computational Neuroscience - interactive track and course project (128 hours)", "date": "2026-07-25", "issuer": "Neuromatch Academy", "url": next(x for x in experience if x["id"] == "neuromatch")["certificate"]}],
        "publications": [{"name": x["title"], "publisher": x.get("status", x["venue"]), "releaseDate": str(x["date"]), "url": x.get("paperurl", x["doiurl"]), "summary": x["excerpt"]} for x in pubs],
        "portfolio": [{"name": x["title"], "url": p["website"].rstrip("/") + x.get("detail", "/projects/" + x["id"].lower() + "/"), "summary": x["summary"]} for x in projects],
        "skills": [{"name": x["title"], "keywords": [x["text"]]} for x in p["skills"]],
        "languages": [{"language": "Chinese", "fluency": "Native"}, {"language": "English", "fluency": p["ielts"]}],
        "interests": [{"name": "Research", "keywords": [p["interests"]]}], "references": [], "presentations": [], "teaching": []}
    (ROOT / "_data/cv.json").write_text(json.dumps(cv, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated two TeX bodies, JSON CV, and {len(projects)} project routes.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cv-dir", type=Path, default=ROOT.parent / "CV")
    build(parser.parse_args().cv_dir)
