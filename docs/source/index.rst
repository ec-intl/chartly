.. chartly documentation master file, created by
   sphinx-quickstart on Wed Oct 16 16:05:42 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Chartly
========

Overview
--------

**Chartly** is a simple plotting tool designed to help users create scientific plots with ease.

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

The Chartly package currently has eight (8) available scientific plots that can be created, namely:

- Line Plot
- Histogram
- Contour Plot
- Normal Probability Plot
- Cumulative Distribution Function Plot
- Normal Cumulative Distribution Function Plot
- Density Plot
- Box Plot

Users can plot these scientific plots by creating a `Chart` instance and overlaying the plots on the figure.

When creating a `Chart` instance, users can set up and label the main figure by passing a dictionary of arguments to the `Chart` class.

Keys:

- `super_title` (str): The title of the main figure.
- `super_xlabel` (str): The x-axis label of the main figure.
- `super_ylabel` (str): The y-axis label of the main figure.
- `share_axes` (bool): Whether to share the y-axes across all subplots. Default is True.

.. code-block:: python

   import chartly
   import numpy as np

   # 1. Define Some Data
   data = np.random.randn(100)

   # 2. Define the main figure labels
   super_axes_labels = {"super_title": "Simple Example", "super_xlabel": "X", "super_ylabel": "Y"}

   # 3. Create a chart instance
   plot = chartly.Chart(super_axes_labels)

To create a plot, a subplot must be created by calling the `new_subplot` method.

.. code-block:: python

   # 4. Create a subplot to overlay the plot
   plot.new_subplot()

After the subplot is created, users can overlay the plots on the main figure by calling the `overlay` method.

Users can create a plot by passing a dictionary of arguments to the `overlay` method. The dictionary should contain the following keys:

- `data`: The data that will be plotted.
- `plot`: The type of plot to be created.

Users can also customize and label the plots by including the following keys in the dictionary:

- `axes_labels`: A dictionary containing the labels of the subplot.
- `customs`: A dictionary containing the customization options of the plot.

 Each plot type has its own customization options. Please continue reading to see the customization options available for each plot type.

.. code-block:: python

   # 5. Overlay a line plot on the subplot
   axes_labels = {"linelabel": "Example Line Label"}
   customs = {"linestyle": "dashdot", "color": "mediumslateblue"}

   payload = {"plot": "line_plot", "data": data, "axes_labels": axes_labels, "customs": customs}
   plot.overlay(payload)


If the user desires multiple subplots, they must call the `new_subplot` method again to create a new subplot. Finally, the figure can be rendered by calling the `Chart` instance.


.. code-block:: python

   # 5. Render the main figure
   plot()

.. image:: https://chartly.s3.amazonaws.com/static/img/plot_index_eg.jpg
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
