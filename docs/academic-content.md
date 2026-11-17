# Academic content workflow

Shared content lives in `_data/profile.yml`, `_data/experience.yml`, `_data/courses.yml`, `_data/projects.yml`, and publication front matter under `_publications/`.

Certified independent courses, reading and the academic timeline live in `_data/independent_study.yml`, `_data/reading.yml` and `_data/journey.yml`. The main CV includes all four reading records. `main_cv_grade: false` keeps a course's grade in the complete record while omitting that grade from the main CV.

From the repository root, with Python and PyYAML installed:

```powershell
python scripts/build_academic_content.py
```

This generates the compatibility JSON CV, project detail routes, and the two TeX bodies in the sibling `../CV/generated/` directory. Main-CV engineering projects are selected with `main_cv: true`; homepage research is selected with `featured: true`. The Full CV includes all projects in priority order. Nullable course grades are rendered as completion-only entries.

Compile `../CV/main.tex` and `../CV/full.tex` with TeX Live, then publish `main.pdf` as `files/Yanzhe_Zhao_CV.pdf` and `full.pdf` as `files/Yanzhe_Zhao_Full_CV.pdf`. Keep the familiar local copies `../CV/CV.pdf` and `../CV/CV_Full.pdf` synchronized.

The entry points use `../CV/academic-style.tex` and `../CV/profile1.png`. Their canonical local location remains outside the Pages repository.

Build the site with the existing Docker setup:

```powershell
docker compose run --rm jekyll-site bash -lc "bundle install && bundle exec jekyll build --config _config.yml,_config_docker.yml"
```

Publication status is supplied by the author. Preserve the distinction between preprints, journal submission/review, and formally published proceedings. Review statuses whenever updating the CV.

## Image sources

- Portrait: original `../CV/profile1.png`; existing web derivative `images/profile-web.jpg`.
- HP-GSBS EEG figure: `https://github.com/JustinZHAO-05/HP-GSBS-SoftwareX-Reproducibility/blob/main/figures/figure3_eeg_application.png`.
- Temporal irreversibility figure: rendered from `https://github.com/JustinZHAO-05/observation-architecture-temporal-irreversibility/blob/main/paper/figures/fig01.pdf`.
- Neuromatch figure: `https://github.com/JustinZHAO-05/Temporal-Persistence-of-Perceptual-Inference-by-Group-Doraemon-Neuromatch-CN-2026/blob/main/perceptual_arbitration/results/figures/figure_04_posterior_state_occupancy.png`.

Original scientific figures retain their source values and labels. The HTML/CSS design is implemented separately from the planning mockups.

- Cognitive Science cover: `https://cupcore2.bluefusesystems.com/core/resources/custom-content/uploads/sites/30/2022/08/Bermudez-cover.jpg`.
- Dayan and Abbott cover: `https://mit-press-new-us.imgix.net/covers/9780262541855.jpg?w=400`.
- Timeline engineering photo: the existing public `images/projects/eight-cable-robot.jpg` asset.

## Intellectual journey

The two essay bodies are in `_includes/journey-essay-en.md` and `_includes/journey-essay-zh.md`. English precedes Chinese. The import script preserves the supplied prose, converts titles to anchored headings, and applies only the approved relative anonymization. The unmodified private attachment is not copied into the repository.

```powershell
python scripts/import_journey_essay.py "<path-to-approved-original-text>" --replacements "<private-rules.json>" --check
python -m unittest discover -s scripts/tests -v
```

KaTeX 0.19.1 is vendored from the official npm package under `assets/vendor/katex/`, including its license and fonts. It loads only on the essay page; local assets keep the article independent of a third-party CDN. Raw formulas remain in the source when JavaScript is unavailable.

Keep the original attachment and replacement rules outside the public repository. Only approved anonymized prose is published.
