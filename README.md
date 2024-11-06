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

```shell
pip install chartly
```

## Example

Scenario: After collecting data from a sample, an investigator wants to visualize the spread of his data, and also determine
whether the sample data fits a normal distribution. 

Here is how Chartly can help the investigator meet his goals.

```python
from chartly import chartly
import numpy as np

# define main figure labels
args = {"super_title": "Investigating a Dataset's Distribution", "super_xlabel": "X", "super_ylabel": "Y", "share_axes": False}

# initialize a main figure
chart = chartly.Chart(args)

# Define the sample data
data =  np.random.randn(200)

# Plot names of the desired plots
plots = ["probability_plot", "dotplot", "normal_cdf"]

for plot in plots:
    # Create a subplot
    chart.new_subplot({"plot": plot, "data": data, "axes_labels": {"title": plot}})

chart()
```

![Example Output](https://chartly.s3.amazonaws.com/static/img/readme_eg.jpg)
