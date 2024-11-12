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

"""Scatter the data"""

# 1.1 Initialize a figure to plot the scatter plot
args = {"super_title": "Scatter of the Sample Data", "super_xlabel": "X", "super_ylabel": "Y"}
chart = chartly.Chart(args)

# 1.2 Define data
x_range = np.arange(200)
sample_data =  np.random.randn(200)

# 1.3 Create Subplot and plot scatter plot
customs = {"color": "royalblue", "size": 50, "marker": "o"}
data = [x_range, sample_data]

chart.new_subplot({"plot": "scatter", "data": data, "customs": customs})

# 1.4 Display the figure
chart()
```

![Example Output](https://chartly.s3.amazonaws.com/static/img/readme_scatter_eg.jpg)


```python
"""Investigate the Distribution of the data using Chartly."""

# 2.1 Define main figure labels
args = {"super_title": "Investigating a Dataset's Distribution", "super_xlabel": "X", "super_ylabel": "Y", "share_axes": False}

# 2.2 initialize a new figure
chart = chartly.Chart(args)

# 2.3 Determine the distribution of the sample data using a dot plot, probability plot and a normal cdf plot.
plots = ["probability_plot", "dotplot", "normal_cdf"]

for plot in plots:
    chart.new_subplot({"plot": plot, "data": sample_data, "axes_labels": {"title": plot}})

# 2.4 Display the figure
chart()
```

![Example Output](https://chartly.s3.amazonaws.com/static/img/readme_eg.jpg)


From the normal probability plot, we see that the line of best fit produced fits the data i.e. most of the points lie on or very close to the line. This suggests that the data has a normal distribution.
This is supported by the dot plot, where the plot's shape resembles the bell curve shape distincitive to the normal distribution, and the normal CDF plot, where the CDF of the data falls very closely to the CDF we expect of a standard normal distribution.

However, if we look closely, we see that the points on the negative end of the plot are very light, suggesting that the data is negatively skewed. This is confirmed by the density plot, where we see that the more positive end of the distribution is heavier that its more negative end.

Given this, the investigator can conclude that the sample has a negatively skewed normal distribution, with a mean of 0.03 and a standard deviation of 0.96.
