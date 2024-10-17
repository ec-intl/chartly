Chartly.Plot Usage Guide
=========================

The Plot Class allows users to plot a single plot at a time on a specified axis. The Plot Class requires a dictionary of arguments to be passed to the class. The following keys are required in the dictionary:

- `data`: The data that will be plotted.
- `ax`: The axis object that the plot will be plotted on.
- `fig`: The figure object that the plot will be plotted on.


There are currently 9 different plot types that can be created using the Plot Class. The Plot Class also allows users to customize these plot by passing additional arguments in the dictionary. The following arguments can be passed to the dictionary:

- `axes_labels`: A dictionary containing the x, y, and title labels, and the scale for the plot.
- `gen_plot_args`: A dictionary containing additional arguments for a generic plot, such as color, linestyle, etc.
- `hist_args`: A dictionary containing additional arguments for a histogram plot, such as color, bins, etc.
- `timeseries_args`: A dictionary containing additional arguments for a time series plot, such as color, linestyle, etc.
- `cdf_args`: A dictionary containing additional arguments for a cumulative distribution function plot, such as color, linestyle, etc.
- `boxplot_args`: A dictionary containing additional arguments for a boxplot plot, such as color, notch, etc.
- `norm_cdf_args`: A dictionary containing additional arguments for a normal cumulative distribution function plot, such as color etc.
- `density_args`: A dictionary containing additional arguments for a density plot, such as color, fill, etc.
- `prob_plot_args`: A dictionary containing additional arguments for a probability plot, such as color etc.
- `contour_args`: A dictionary containing additional arguments for a contour plot, such as color, filled, etc.

Examples
--------

Generic Plot
~~~~~~~~~~~~

The Generic Plot is a simple plot that can be used to plot any type of data. The plot is created using the `generic_plot` method. Users can pass both x and y data or just y data to the plot.

.. code-block:: python

    import matplotlib.pyplot as plt
    import chartly

    fig, ax = plt.subplots()

    # Only y data
    data = np.random.randn(100)

    # customize the plot
    gen_plot_args = {"color": "red", "linestyle": "--"}
    # label the plot
    axes_labels = {"ylabel": "Y", "title": "Generic Plot Example"}

    # set the arguments
    args = {"data": data, "ax": ax, "fig": fig, "gen_plot_args": gen_plot_args, "axes_labels": axes_labels}
    plot = chartly.Plot(args)

    plot.generic_plot()

    plt.show()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/gen_plot_only_y.jpg
    :alt: GenericPlotOnlyY
    :align: center


.. code-block:: python

    import matplotlib.pyplot as plt
    import chartly

    fig, ax = plt.subplots()

    # x and y data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # customize the plot
    gen_plot_args = {"color": "mediumpurple", "linestyle": "--"}

    # label the plot
    axes_labels = {"ylabel": "Y", "xlabel": "X", "title": "Generic Plot Example with X & Y"}

    args = {"data": [x, y], "ax": ax, "fig": fig, "gen_plot_args": gen_plot_args, "axes_labels": axes_labels}
    plot = chartly.Plot(args)

    plot.generic_plot()

    plt.show()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/gen_plot_x_y.jpg
    :alt: GenericPlotXY
    :align: center


Histogram
~~~~~~~~~

A histogram plot can be created using the `plot_histogram` method.


.. code-block:: python

    import matplotlib.pyplot as plt
    import chartly

    fig, ax = plt.subplots()

    data = np.random.randn(1000)

    # customize the plot

    histogram_args = {"color": "salmon", "num_bins": 30}

    # label the plot
    axes_labels = {"ylabel": "Frequency", "xlabel": "Value", "title": "Histogram Plot Example"}

    args = {"data": data, "ax": ax, "fig": fig, "histogram_args": histogram_args, "axes_labels": axes_labels}
    plot = chartly.Plot(args)

    plot.plot_histogram()

    plt.show()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/hist_eg.jpg
    :alt: HistogramExample
    :align: center


Contour Plot
~~~~~~~~~~~~

Contour plots can be created using the `plot_contour` method. The contour plot requires 2D arrays of X, Y and Z data to be passed to the plot.

.. code-block:: python

    import matplotlib.pyplot as plt
    import chartly

    fig, ax = plt.subplots()

    x = np.linspace(-3.0, 3.0, 100)
    y = np.linspace(-3.0, 3.0, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.cos(X/3) * np.sin(Y/3)

    # label the plot
    axes_labels = {"xlabel": "X", "ylabel": "Y", "title": "Contour Plot Example"}

    args = {"data": [X, Y, Z], "ax": ax, "fig": fig, "axes_labels": axes_labels}
    plot = chartly.Plot(args)

    plot.plot_contour()

    plt.show()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/contour_eg.jpg
    :alt: ContourExample
    :align: center


Normal Probability Plot
~~~~~~~~~~~~~~~~~~~~~~~

The normal probability plot is used to determine if a dataset is approximately normally distributed. A normal probability plot can be created using the `plot_probability_plot` method. The normal probability plot requires a 1D array of data to be passed to the plot.

.. code-block:: python

    import matplotlib.pyplot as plt
    import chartly

    fig, ax = plt.subplots()

    data = np.random.randn(100)

    # customize the plot
    prob_plot_args = {"color": "firebrick"}

    # label the plot
    axes_labels = {"title": "Normal Probability Plot Example"}

    args = {"data": data, "ax": ax, "fig": fig, "axes_labels": axes_labels, "prob_plot_args": prob_plot_args}
    plot = chartly.Plot(args)

    plot.plot_probability_plot()

    plt.show()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/norm_prob_eg.jpg
    :alt: NormalProbabilityExample
    :align: center

Normal Cumulative Distribution Function Plot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CDF of a dataset can be compared to the CDF of a normal distribution using the normal CDF plot. The normal CDF plot can be created using the `plot_normal_cdf` method. Users can pass multiple datasets to the plot.


.. code-block:: python

    import matplotlib.pyplot as plt
    import chartly

    fig, ax = plt.subplots()

    dataset_one = np.random.exponential(scale=1.0, size=500)
    dataset_two = np.random.normal(loc=20, scale=1, size=500)
    dataset_three = np.random.gamma(2, 2, 500)
    data = [dataset_one, dataset_two, dataset_three]


    # label the plot
    axes_labels = {"title": "Normal Cumulative Distribution Function Plot Example"}

    args = {"data": data, "ax": ax, "fig": fig, "axes_labels": axes_labels}
    plot = chartly.Plot(args)

    plot.plot_normal_cdf()

    plt.show()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/norm_cdf_eg.jpg
    :alt: NormalCDFExample
    :align: center

