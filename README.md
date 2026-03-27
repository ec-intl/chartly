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

`chartly` is a lightweight scientific plotting library designed to simplify the process of building visualizations. It provides a clean and intuitive interface for generating statistical plots, overlays, and multi-plot figures without requiring complex setup or boilerplate code.

Whether you are exploring distributions, comparing datasets, or building composite visualizations, Chartly enables you to move from data to insight with minimal effort.

Chartly’s interface is built around a few core methods:

- `add_subplot(...)` → create a new subplot  
- `add_subplots(...)` → create multiple subplots at once  
- `add_overlay(...)` → add additional plots to an existing subplot  
- `render()` → display the final figure  


## Project Status

Here's the current status of our workflows:

| Workflow                | Status |
|-------------------------|--------|
| Testing Suite  | [![Continuous-Integration](https://github.com/ec-intl/chartly/actions/workflows/ci.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/ci.yml) |
| Deployment Suite | [![Continuous-Deployment](https://github.com/ec-intl/chartly/actions/workflows/cd.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/cd.yml)|
| Sphinx Documentation | [![Sphinx-docs](https://github.com/ec-intl/chartly/actions/workflows/docs.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/docs.yml) |
| Guard Main Branch | [![Guard Main Branch](https://github.com/ec-intl/chartly/actions/workflows/guard.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/guard.yml) |
| Code Quality Checker | [![Lint Codebase](https://github.com/ec-intl/chartly/actions/workflows/super-linter.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/super-linter.yml) |


## Components

The Chartly codebase is organized as follows:

```plaintext  
.
├── chartly/
│   ├── base.py
│   ├── chartly.py
│   ├── charts.py
│   ├── utilities.py
│   └── tests/
│       ├── __init__.py
│       └── test_chartly.py
├── docs/
│   ├── __init__.py
│   ├── source/
│   │   ├── conf.py
│   │   ├── index.rst
│   │   ├── Plot.rst
│   │   └── Multiplots.rst
├── requirements/
│   ├── testing.txt
│   ├── staging.txt
│   └── production.txt
├── LICENSE
├── MANIFEST.in
├── README.md
├── requirements.txt
├── setup.py
└── VERSION
```


## Requirements

Chartly depends on the following core scientific Python libraries:

- matplotlib >= 3.8  
- numpy >= 2.0  
- scipy >= 1.14  
- seaborn >= 0.13  


## Installation

Install Chartly directly from PyPI:

```bash
pip install chartly
```


## Examples

The following examples demonstrate how to use Chartly for common visualization tasks, from simple plots to more advanced multi-plot configurations.

---
### Single Plot

The following example generates a scatter plot with custom styling.

```python
"""Scatter Plot of Sample Data"""

import chartly
import numpy as np

args = {
    "super_title": "Scatter of the Sample Data",
    "super_xlabel": "X",
    "super_ylabel": "Y",
}

chart = chartly.Chart(args)

x_range = np.arange(200)
sample_data = np.random.randn(200)

chart.add_subplot(
    "scatter",
    [x_range, sample_data],
    customs={"color": "royalblue", "size": 50, "marker": "o"},
)

chart.render()
```

This visualization highlights how Chartly supports customization while maintaining a simple interface.

<img width="1964" height="795" alt="image" src="https://github.com/user-attachments/assets/5cd441c8-7576-4763-8147-207acb4d804d" />

---

### Multiple Subplots

Chartly simplifies the process of generating multiple related plots within a single figure.

```python
"""Distribution Analysis Using Multiple Subplots"""

import chartly
import numpy as np

args = {
    "super_title": "Distribution Analysis",
    "super_xlabel": "X",
    "super_ylabel": "Y",
    "share_axes": False,
}

chart = chartly.Chart(args)

data = np.random.randn(200)

chart.add_subplots(
    ["probability_plot", "dotplot", "normal_cdf"],
    data=data,
)

chart.render()
```

This example produces multiple statistical views of the same dataset without requiring loops or manual payload construction.

<img width="1965" height="795" alt="image" src="https://github.com/user-attachments/assets/8622b05d-0d67-4640-8c24-eb36f64b4318" />

---

### Overlay Example

Chartly also supports overlaying multiple plots within the same subplot for richer analysis.

```python
"""Overlaying Density on a Histogram"""

import chartly
import numpy as np

args = {
    "super_title": "Overlay Example",
    "super_xlabel": "X",
    "super_ylabel": "Y",
}

chart = chartly.Chart(args)

data = np.random.randn(1000)

chart.add_subplot("histogram", data)
chart.add_overlay("density", data)

chart.render()
```

In this example, a density curve is layered on top of a histogram, allowing both distribution and frequency to be visualized together.

<img width="1965" height="795" alt="image" src="https://github.com/user-attachments/assets/e3e094ee-5f68-4e99-bc38-ef487a6df6dc" />

---

## Documentation

Full documentation is available via Sphinx:

https://ec-intl.github.io/chartly/
