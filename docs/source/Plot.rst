Chartly's Charts Usage Guide
============================

The Chartly package currently has eight (8) available scientific plots that can be created using the package. Each plot requires a dictionary of arguments to be passed to the class. The following keys are required in the dictionary:

- `data`: The data that will be plotted.

The plots can also be customized by passing a `customs` dictionaty to the class. Each plot type has its own customization options.

Charts
--------

Line Plot
~~~~~~~~~~~~

The Line Plot is a simple plot that can be used to plot any type of data. The plot is created using the `LinePlot` class. Users can pass both x and y data or just y data to the plot.

The following customization options are available for the Line Plot:

- `color` (str): The color of the line.
- `linestyle` (str): The style of the line.

.. code-block:: python

    import chartly

    # Only y data
    data = np.random.randn(100)

    # customize the plot
    customs = {"color": "red", "linestyle": "--"}
    # label the plot
    axes_labels = {"ylabel": "Y", "title": "Generic Plot Example"}

    # set the arguments
    args = {"data": data, "customs": customs, "axes_labels": axes_labels}
    plot = chartly.LinePlot(args)

    plot()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/gen_plot_only_y.jpg
    :alt: GenericPlotOnlyY
    :align: center


.. code-block:: python
    import chartly

    # x and y data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # customize the plot
    customs = {"color": "mediumpurple", "linestyle": "--"}

    # label the plot
    axes_labels = {"ylabel": "Y", "xlabel": "X", "title": "Generic Plot Example with X & Y"}

    args = {"data": [x, y], "customs": customs, "axes_labels": axes_labels}
    plot = chartly.LinePlot(args)

    plot()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/gen_plot_x_y.jpg
    :alt: GenericPlotXY
    :align: center


Histogram
~~~~~~~~~

A histogram plot can be created using the `Histogram` class. The histogram plot requires a 1D array of data to be passed to the plot. The following customization options are available for the histogram plot:

- `color` (str): The color of the histogram.
- `num_bins` (int): The number of bins in the histogram.
- `ran` (tuple): The range of the histogram.

.. code-block:: python

    import chartly

    data = np.random.randn(1000)

    # customize the plot
    customs = {"color": "salmon", "num_bins": 30}

    # label the plot
    axes_labels = {"ylabel": "Frequency", "xlabel": "Value", "title": "Histogram Plot Example"}

    args = {"data": data, "customs": customs, "axes_labels": axes_labels}
    plot = chartly.Histogram(args)

    plot()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/hist_eg.jpg
    :alt: HistogramExample
    :align: center


Contour Plot
~~~~~~~~~~~~

Contour plots can be created using the `Contour` class. The contour plot requires 2D arrays of X, Y and Z data to be passed to the plot. The following customization options are available for the contour plot:

- `color` (str): The color of the contour plot. Ensure that the `cmap` is set to None.
- `levels` (int): The number of contour levels.
- `cmap` (str): The colormap of the contour plot.
- `filled` (bool): Whether the contour plot is filled or not.
- `fsize` (int): The font size of the contour labels.

.. code-block:: python

    import chartly

    x = np.linspace(-3.0, 3.0, 100)
    y = np.linspace(-3.0, 3.0, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.cos(X/3) * np.sin(Y/3)

    # customize the plot
    customs = {"cmap": "magma", "fsize": 14, "filled": True}

    # label the plot
    axes_labels = {"xlabel": "X", "ylabel": "Y", "title": "Contour Plot Example"}

    args = {"data": [X, Y, Z], "axes_labels": axes_labels, "customs": customs}
    plot = p.Contour(args)
    plot()


.. image:: https://clidapp.s3.amazonaws.com/static/server/img/contour_eg.jpg
    :alt: ContourExample
    :align: center


Normal Probability Plot
~~~~~~~~~~~~~~~~~~~~~~~

The normal probability plot is used to determine if a dataset is approximately normally distributed. A normal probability plot can be created using the `ProbabilityPlot` class. The normal probability plot requires a 1D array of data to be passed to the plot. The following customization options are available for the normal probability plot:

- `color` (str): The color of the markers of the plot.

.. code-block:: python

    import chartly

    data = np.random.randn(100)

    # customize the plot
    customs = {"color": "firebrick"}

    # label the plot
    axes_labels = {"title": "Normal Probability Plot Example"}

    args = {"data": data, "axes_labels": axes_labels, "customs": customs}
    plot = chartly.ProbabilityPlot(args)

    plot()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/norm_prob_eg.jpg
    :alt: NormalProbabilityExample
    :align: center


Cumulative Distribution Function Plot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CDF plot of a dataset can be created using the `CDF` class. The CDF plot requires a 1D array of data to be passed to the plot. The following customization options are available for the CDF plot:

- `color` (str): The color of the CDF plot.


.. code-block:: python

    import chartly

    data = np.random.exponential(scale=1.0, size=500)

    # label the plot
    axes_labels = {
        "title": "Cumulative Distribution Function Plot Example",
        "ylabel": "Probability",
        "linelabel": "CDF",
    }

    args = {"data": data, "axes_labels": axes_labels}
    plot = chartly.CDF(args)

    plot()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/cdf_eg.jpg
    :alt: NormalCDFExample
    :align: center


Normal Cumulative Distribution Function Plot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CDF of a dataset can be compared to the CDF of a normal distribution using the normal CDF plot. The normal CDF plot can be created using the `normal_cdf` method. Users can pass multiple datasets to the plot.


.. code-block:: python

    import chartly

    dataset_one = np.random.exponential(scale=1.0, size=500)
    dataset_two = np.random.normal(loc=20, scale=1, size=500)
    dataset_three = np.random.gamma(2, 2, 500)
    data = [dataset_one, dataset_two, dataset_three]


    # label the plot
    axes_labels = {"title": "Normal Cumulative Distribution Function Plot Example"}

    args = {"data": data, "axes_labels": axes_labels}
    plot = chartly.NormalCDF(args)

    plot()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/norm_cdf_eg.jpg
    :alt: NormalCDFExample
    :align: center


Density Plot
~~~~~~~~~~~~

The density function of a distribution can be created using the `Density` class. The `Density` plot requires a 1D array of data to be passed to the plot. The following customization options are available for the CDF plot:


- `color` (str): The color of the density plot.
- `fill` (bool): Whether the density plot is filled or not.


.. code-block:: python

    import chartly

    data = np.random.exponential(scale=1.0, size=500)

    # label the plot
    axes_labels = {
    "title": "Density Plot Example", "ylabel": "Probability", "linelabel": "CDF",
    }

    customs = {"fill": True, "color": "mediumvioletred", "label": "density"}
    args = {"data": data, "axes_labels": axes_labels, "customs": customs}
    plot = chartly.CDF(args)

    plot()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/density_eg.jpg
    :alt: NormalCDFExample
    :align: center


Box Plot
~~~~~~~~~~~~

A boxplot of one or more datasets can be plotted using the `BoxPlot` class. A dataset list or a list of dataset lists can be passed to the `BoxPlot` plot. The following customization options are available for the `BoxPlot` plot:


- `showfliers` (bool): Whether to show the outliers in the boxplot.
- `boxlabels` (list): The labels of the boxplots.


.. code-block:: python

    import chartly

    dataset_one = np.random.exponential(scale=1.0, size=500)
    dataset_two = np.random.normal(loc=2, scale=1, size=500)
    dataset_three = np.random.gamma(2, 2, 500)
    data = [dataset_one, dataset_two, dataset_three]

    # label the plot
    axes_labels = {"title": "BoxPlot Example"}

    customs = {"showfliers": False}
    args = {"data": data, "axes_labels": axes_labels, "customs": customs}
    plot = chartly.BoxPlot(args)

    plot()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/boxplot_eg.jpg
    :alt: NormalCDFExample
    :align: center

