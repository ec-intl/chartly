# plotting Package

![GitHub license](https://img.shields.io/github/license/ec-intl/plotting)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/ec-intl/plotting)
![GitHub issues](https://img.shields.io/github/issues/ec-intl/plotting)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ec-intl/plotting)
![GitHub contributors](https://img.shields.io/github/contributors/ec-intl/plotting)
![GitHub last commit](https://img.shields.io/github/last-commit/ec-intl/plotting)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ec-intl/plotting)
![GitHub top language](https://img.shields.io/github/languages/top/ec-intl/plotting)
![GitHub search hit counter](https://img.shields.io/github/search/ec-intl/plotting/plotting)
![GitHub stars](https://img.shields.io/github/stars/ec-intl/plotting)
![GitHub watchers](https://img.shields.io/github/watchers/ec-intl/plotting)

`plotting` is a lightweight Python package designed to plot and customize multiple subplots and overlays onto one master plot.


## Project Status

Here's the current status of our workflows:

| Workflow                | Status |
|-------------------------|--------|
| Testing Suite  | [![Continuous-Integration](https://github.com/ec-intl/plotting/actions/workflows/ci.yml/badge.svg)](https://github.com/ec-intl/plotting/actions/workflows/ci.yml) |
| Deployment Suite | [![Continuous-Deployment](https://github.com/ec-intl/plotting/actions/workflows/cd.yml/badge.svg)](https://github.com/ec-intl/plotting/actions/workflows/cd.yml)|
| Sphinx Documentation           | [![Sphinx-docs](https://github.com/ec-intl/plotting/actions/workflows/docs.yml/badge.svg)](https://github.com/ec-intl/plotting/actions/workflows/docs.yml) |
| Guard Main Branch       | [![Guard Main Branch](https://github.com/ec-intl/plotting/actions/workflows/guard.yml/badge.svg)](https://github.com/ec-intl/plotting/actions/workflows/guard.yml) |
| Code Quality Checker    | [![Lint Codebase](https://github.com/ec-intl/plotting/actions/workflows/super-linter.yml/badge.svg)](https://github.com/ec-intl/plotting/actions/workflows/super-linter.yml) |

## Components

The plotting's codebase structure is as shown below:

```plaintext
.
├── LICENSE
├── README.md
├── MANIFEST.in
├── VERSION
├── Dockerfile
├── docker-compose.yml
├── CHANGELOG.md
├── docs
│   ├── index.html
│   ├── static
|   │   ├── css
|   |   │   └── site.css
|   |   └── js
|   |       └── site.js
├── requirements
│   ├── testing.txt
│   ├── staging.txt
│   └── production.txt
├── requirements.txt
├── setup.py
├── scripts
│   ├── ci
│   │   └── run-ci.sh
│   └── dev
│       └── sleeping_daemon.sh
└── src
│   ├── plotting
│   │   ├── __init__.py
│   │   └── plotting.py
│   └── tests
│   │   ├── __init__.py
│   │   └── test_plotting.py
```
