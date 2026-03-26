.. chartly documentation master file, created by
   sphinx-quickstart on Wed Oct 16 16:05:42 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Chartly
========

Overview
--------

**Chartly** is a simple plotting tool designed to help users create scientific plots with ease. Whether you want to test a distribution for normality or to plot contours onto a map of the globe, chartly can help you achieve your scientific plot with minimal effort. Chartly also allows users to plot multiple overlays and subplots onto the same figure.


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

Chartly allows users to build plots by first creating a main figure and then adding subplots to the figure. To initialize a main figure, users can create a `Chart` instance. Users can also label and customize the main figure by passing an optional dictionary. The dictionary should contain the following keys:

- `super_title` (str): The title of the main figure.
- `super_xlabel` (str): The x-axis label of the main figure.
- `super_ylabel` (str): The y-axis label of the main figure.
- `share_axes` (bool): Whether to share the y-axes across all subplots. Default is True.

.. code-block:: python

   import chartly
   import numpy as np

   # 1. Define the main figure labels
   super_axes_labels = {"super_title": "Usage Of Chartly Example", "super_xlabel": "X", "super_ylabel": "Y", "share_axes": False}

   # 2. Initialize a main figure by creating a chart instance
   plot = chartly.Chart(super_axes_labels)


To create a plot, users can directly add a subplot with ``add_subplot(...)``.
Additional plots can be added to the same subplot with ``add_overlay(...)``.
This keeps the public interface simpler by avoiding manual payload
dictionaries.


.. code-block:: python

   # 3. Define Some Data
   data = np.random.randn(100)

   # 4. Add a subplot directly
   plot.add_subplot("histogram", data)


To overlay a new plot onto the current subplot, users can call
``add_overlay(...)`` and pass the plot type and data directly.

.. code-block:: python

   # 5. Overlay another plot
   plot.add_overlay("density", data)


To add another subplot, users can call ``add_subplot(...)`` again with the
new plot type and data.

.. code-block:: python

   # 6. Add another subplot
   plot.add_subplot("boxplot", data)


Users can also customize the axes of each subplot. 

- Users can change the scale of the x and y axes from linear to log. They can also change the base of the log scale. If the base is changed, ensure that the subplots are not sharing axes.


.. code-block:: python

   # 7. Define a random exponential function
   exp_func = lambda x: np.e ** (-500 * x + 2)

   x = np.linspace(0, 1, num=100)
   y = list(map(exp_func, x))
   
   # 8. Add customized subplot
   plot.add_subplot(
      "line_plot",
      y,
      axes_labels={"scale": "semilogy", "base": 10, "linelabel": "Semilogy Line"},
   )


Finally, the figure can be rendered by calling ``render()``.

.. code-block:: python

   # 9. Render the main figure
   plot.render()

To save the figure that was rendered, users can call the `save` method. The default file format is `eps` and the default file name is `chartly_plot`. To change the file format and name, update the plot's properties.


.. code-block:: python

   # 10. Save the figure with a different file format and name
   plot.format = "jpg"
   plot.fname = "my_plot"
   plot.save()

.. image:: https://chartly.s3.amazonaws.com/static/img/my_plot.jpg
    :alt: SimpleUsageOfChartlyExample
    :align: center
    :height: 500px

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