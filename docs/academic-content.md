# Academic content workflow

Shared content lives in `_data/profile.yml`, `_data/experience.yml`, `_data/courses.yml`, `_data/projects.yml`, and publication front matter under `_publications/`.

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
