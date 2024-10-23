.. chartly documentation master file, created by
   sphinx-quickstart on Wed Oct 16 16:05:42 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Chartly
========

Overview
--------

**Chartly** is a simple tool designed to help users create scientific plots with ease. The package is built on top of the `matplotlib` and `seaborn` libraries, and it provides a simple interface for creating and customizing scientific plots.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Requirements
------------

The chartly package requires the following packages:

- `matplotlib` >= 3.9.1
- `numpy` >= 1.26.4
- `scipy` >= 1.14.0
- `seaborn` >= 0.11.0

Installation
------------

To install the chartly package, run the following command:

.. code-block:: shell

    pip install chartly

Usage
-----

To plot a scientific chart using the chartly package, you need to follow these steps:

1. Import the chartly package.
2. Create a plot instance.
3. Call the plot instance.


Here is an example of how to use the chartly package:

.. code-block:: python

    import chartly
    import numpy as np

    data = np.random.randn(100)
    args = {"data": data}
    plot = chartly.LinePlot(args)

    plot()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/plot_index_eg.jpg
    :alt: SimpleExampleResult
    :align: center

.. toctree::
   :maxdepth: 2

   Plot

.. toctree::
   :maxdepth: 2

   Multiplots


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
