.. chartly documentation master file, created by
   sphinx-quickstart on Wed Oct 16 16:05:42 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Chartly
========

Overview
--------

**Chartly** is a simple tool that allows you to create plots using minimal lines of code.



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
To use the chartly package, you need to import the package and create a plot object.
There are two main methods that you can use to create a plot:

- `Plot`: This method plots a single plot at a time on a specified axis.
- `Multiplots`: This method plots multiple plots and overlays on a single figure.

Here is an example of how to use the chartly package:

.. code-block:: python

    import chartly

    data = np.random.randn(100)
    args = {"data": data}
    plot = chartly.Plot(args)

    plot.generic_plot()


.. image:: https://clidapp.s3.amazonaws.com/static/server/img/plot_index_eg.jpg
    :alt: SimpleExampleResult
    :align: center

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
