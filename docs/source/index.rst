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

Chartly allows users to build plots by first creating a main figure and then adding subplots to the figure. To initialize a main figure, users can create a `Chart` instance. Users can also label and customize the main figure my passing an optional dictionary. The dictionary should contain the following keys:

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


To create a plot, a user must create a subplot by calling the `new_subplot` method and passing it an optional dictionary of arguments. The dictionary should contain the following keys:

- `data`: The data that will be plotted.
- `plot`: The type of plot to be created.

Users can also customize and label the plots by including the following keys in the dictionary:

- `axes_labels`: A dictionary containing the labels of the subplot.
- `customs`: A dictionary containing the customization options of the plot.


.. code-block:: python

   # 3. Define Some Data
   data = np.random.randn(100)

   # 4. Build the plot dictionary
   plot_payload = {
       "plot": "histogram",
       "data": data,
   }

   # 5. Plot the data
   plot.new_subplot(plot_payload)


To overlay a new plot onto the current subplot, a user can call the `overlay` method and pass it a dictionary of arguments, similar to what is shown above: 


.. code-block:: python

   # 6. build the overlay plot dictionary
   plot_payload = {
       "plot": "density",
       "data": data,
   }

   # 7. Overlay the plot
   plot.overlay(plot_payload)


To add a new subplot, users can call the `new_subplot` method again and pass it a dictionary of arguments.


.. code-block:: python

   # 8. build the plot dictionary
   plot_payload = {
       "plot": "boxplot",
       "data": data,
   }

   # 9. Plot data onto new subplot
   plot.new_subplot(plot_payload)


Users can also customize the axes of each subplot. 

- Users can change the scale of the x and y axes from linear to log. They can also change the base of the log scale. If the base is changed, ensure that the subplots are not sharing axes.


.. code-block:: python

   # 10. Define a random exponential function
   exp_func = lambda x: np.e ** (-500 * x + 2)

   x = np.linspace(0, 1, num=100)
   y = list(map(exp_func, x))
   
   # 11. build the plot dictionary
   plot_payload = {
       "plot": "line_plot",
       "data": y,
       "axes_labels": {"scale": "semilogy", "base": 10, "linelabel": "Semilogy Line"},
   }

   # 12. Plot exponential function
   plot.new_subplot(plot_payload)


Finally, the figure can be rendered by calling the `Chart` instance.


.. code-block:: python

   # 13. Render the main figure
   plot()

To save the figure that was rendered, users can call the `save` method. The default file format is `eps` and the default file name is `chartly_plot`. To change the file format and name, update the plot's properties.


.. code-block:: python

   # 14. Save the figure with a different file format and name
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
