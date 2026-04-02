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

`chartly` is a lightweight scientific plotting library designed to
simplify the process of building visualisations. It provides a clean and
intuitive interface for generating statistical plots, geographic
visualisations, overlays, and multi-plot figures without requiring complex
setup or boilerplate code.

Whether you are exploring distributions, comparing datasets, visualising
geographic data, or building composite visualisations, Chartly enables you
to move from data to insight with minimal effort.

Chartly provides a small set of high-level methods that simplify the
plotting workflow:

- `add_subplot(...)` -> create a new subplot
- `add_subplots(...)` -> create multiple subplots at once
- `add_overlay(...)` -> add additional plots to an existing subplot
- `add_basemap(...)` -> create geographic visualisations using map projections
- `render()` -> display the final figure

## Project Status

Here's the current status of our workflows:

<!-- markdownlint-disable MD013 -->
| Workflow                | Status                                                                                                                                                                     |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Testing Suite           | [![Continuous-Integration](https://github.com/ec-intl/chartly/actions/workflows/ci.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/ci.yml)            |
| Deployment Suite        | [![Continuous-Deployment](https://github.com/ec-intl/chartly/actions/workflows/cd.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/cd.yml)             |
| Sphinx Documentation    | [![Sphinx-docs](https://github.com/ec-intl/chartly/actions/workflows/docs.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/docs.yml)                   |
| Guard Main Branch       | [![Guard Main Branch](https://github.com/ec-intl/chartly/actions/workflows/guard.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/guard.yml)           |
| Code Quality Checker    | [![Lint Codebase](https://github.com/ec-intl/chartly/actions/workflows/super-linter.yml/badge.svg)](https://github.com/ec-intl/chartly/actions/workflows/super-linter.yml) |
<!-- markdownlint-disable MD013 -->

## Components

The Chartly codebase is organised as follows:

```plaintext
.
├── chartly/
│   ├── __init__.py
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
│   │   ├── Multiplots.rst
│   │   └── Basemap.rst
├── requirements/
│   ├── testing.txt
│   ├── staging.txt
│   └── production.txt
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── README.md
├── VERSION
├── requirements.txt
└── setup.py
```

## Installation

Install Chartly directly from PyPI:

```bash
pip install chartly
```

## Examples

The following examples demonstrate how to use Chartly for common
visualisation tasks, from simple plots to more advanced multi-plot
configurations.

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

This visualisation highlights how Chartly supports customisation while
maintaining a simple interface.

![Scatter Plot Example](https://github.com/user-attachments/assets/5cd441c8-7576-4763-8147-207acb4d804d)

---

### Multiple Subplots

Chartly simplifies the process of generating multiple related plots
within a single figure.

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

This example produces multiple statistical views of the same dataset
without requiring loops or manual payload construction.

![Multiple Subplots Example](https://github.com/user-attachments/assets/8622b05d-0d67-4640-8c24-eb36f64b4318)

---

### Overlay Example

Chartly also supports overlaying multiple plots within the same subplot
for richer analysis.

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

In this example, a density curve is layered on top of a histogram,
allowing both distribution and frequency to be visualised together.

![Overlay Example](https://github.com/user-attachments/assets/e3e094ee-5f68-4e99-bc38-ef487a6df6dc)

---

### Basemap

Chartly also supports geographic visualisations with basemaps, making
it possible to overlay contour data on map projections using the same
simplified plotting interface.

```python
"""Simple Basemap Example"""

import chartly
import numpy as np

super_axes_labels = {
    "super_title": "Simple Usage Of Basemap Example",
    "share_axes": False,
}

plot = chartly.Chart(super_axes_labels)

nlats, nlons = 73, 145
delta = 2.0 * np.pi / (nlons - 1)
lats = 0.5 * np.pi - delta * np.indices((nlats, nlons))[0, :, :]
lons = delta * np.indices((nlats, nlons))[1, :, :]
wave = 0.75 * (np.sin(2.0 * lats) ** 8 * np.cos(4.0 * lons))
mean = 0.5 * np.cos(2.0 * lats) * ((np.sin(2.0 * lats)) ** 2 + 2.0)
z = wave + mean

plot.add_basemap(
    lon=lons * 180.0 / np.pi,
    lat=lats * 180.0 / np.pi,
    values=z,
    customs={
        "proj": "eck4",
        "lon_0": 0,
        "draw_countries": True,
        "draw_parallels": True,
        "draw_meridians": True,
        "mask": z < 0,
        "contour": True,
        "hatch": True,
        "hatch_customs": {"type": "mask"},
    },
)

plot.render()
```

This example demonstrates how Chartly can plot contour data on a global
map projection while keeping the user-facing interface minimal and
readable.

![Basemap Example](https://github.com/user-attachments/assets/dcd003f0-b5d6-42b6-a5e5-0386357adef6)

---

## Documentation

Full documentation is available via Sphinx:

[https://ec-intl.github.io/chartly/](https://ec-intl.github.io/chartly/)
