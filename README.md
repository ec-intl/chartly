# chartly Package

![GitHub license](https://img.shields.io/github/license/ec-intl/chartly)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/ec-intl/chartly)
![GitHub issues](https://img.shields.io/github/issues/ec-intl/chartly)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ec-intl/chartly)
![GitHub contributors](https://img.shields.io/github/contributors/ec-intl/chartly)
![GitHub last commit](https://img.shields.io/github/last-commit/ec-intl/chartly)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ec-intl/chartly)
![GitHub top language](https://img.shields.io/github/languages/top/ec-intl/chartly)
![GitHub search hit counter](https://img.shields.io/github/search/ec-intl/chartly/chartly)
![GitHub stars](https://img.shields.io/github/stars/ec-intl/chartly)
![GitHub watchers](https://img.shields.io/github/watchers/ec-intl/chartly)

`chartly` is a simple plotting tool designed to help users create scientific plots with ease. Whether you want to test a distribution for normality or to plot contours onto a map of the globe, chartly can help you achieve your scientific plot with minimal effort. Chartly also allows users to plot multiple overlays and subplots onto the same figure.

## Project Status

Here's the current status of our workflows:

| Workflow                | Status |
|-------------------------|--------|
| Testing Suite  | [![Continuous-Integration](https://github.com/ec-intl/chartly/actions/workflows/ci.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/ci.yml) |
| Deployment Suite | [![Continuous-Deployment](https://github.com/ec-intl/chartly/actions/workflows/cd.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/cd.yml)|
| Sphinx Documentation           | [![Sphinx-docs](https://github.com/ec-intl/chartly/actions/workflows/docs.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/docs.yml) |
| Guard Main Branch       | [![Guard Main Branch](https://github.com/ec-intl/chartly/actions/workflows/guard.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/guard.yml) |
| Code Quality Checker    | [![Lint Codebase](https://github.com/ec-intl/chartly/actions/workflows/super-linter.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/super-linter.yml) |

## Components

The chartly's codebase structure is as shown below:

```plaintext
.
├── chartly/
│   ├── base.py
│   ├── chartly.py
│   ├── charts.py
│   └── utilities.py
│   └── tests/
│   │   ├── __init__.py
│   │   └── test_chartly.py
├── docs/
│   ├── __init__.py
│   ├── source/
|   │   ├── conf.py
|   │   ├── index.rst
|   │   ├── Plot.rst
|   │   └── Multiplots.rst
├── requirements/
│   ├── testing.txt
│   ├── staging.txt
│   └── production.txt
├── LICENSE
├── MANIFEST.in
├── README.md
├── requirements.txt
├── setup.py
└── VERSION
```

## Installation

To install `chartly`, run this command in your command line:

```
pip install chartly
```

## Example

Here is an example on how to use chartly to plot.

```python

import chartly
import numpy as np

# 1. Define Some Data
data = np.random.randn(100)

# 2. Define the main figure labels
super_axes_labels = {"super_title": "Simple Example", "super_xlabel": "X", "super_ylabel": "Y"}

# 3. Create a chart instance
plot = chartly.Chart(super_axes_labels)

# 4. Customize the plot and the axes
axes_labels = {"linelabel": "Example Line Label"}
customs = {"linestyle": "dashdot", "color": "mediumslateblue"}

# 5. Plot the data
payload = {"plot": "line_plot", "data": data, "axes_labels": axes_labels, "customs": customs}
plot.new_subplot(payload)

# 6. Render the main figure
plot()
```

![Example Output](https://clidapp.s3.amazonaws.com/static/server/img/plot_index_eg.jpg)
