Chartly.Multiplots Usage Guide
===============================

The Multiplots Class allows users to plot multiple plots and overlay them on a single figure. The Multiplots Class requires a dictionary of arguments to be passed to the class:

- `super_title` (str): The title of the figure.
- `super_xlabel` (str): The x-axis label of the figure.
- `super_ylabel` (str): The y-axis label of the figure.
- `share_axes` (bool): Whether to share the y-axes across all subplots.


Examples
--------

Overlay Plots
~~~~~~~~~~~~~

The `overlay` method allows users to overlay multiple plots on a single subplot. The overlay method requires a dictionary of arguments to be passed to the method:

- `plot` (str): The type of plot to overlay.
- `data` (list): A list of data that will be plotted.



.. code-block:: python

    import chartly

    # define main figure labels
    args = {"super_title": "Overlay Example", "super_xlabel": "X", "super_ylabel": "Y", "share_axes": False}

    multi = chartly.Multiplots(args)

    # Define Some Data
    data = np.random.normal(loc=2, scale=1, size=1000)

    # Create a subplot
    multi.new_subplot()

    plots = ["histogram", "density"]

    for plot in plots:
        # set up overlay payload
        overlay_payload = {"plot": plot, "data": data, "axes_labels": {}}

        # Overlay a histogram
        multi.overlay(overlay_payload)

    # Overlay a density plot
    overlay_payload = {"plot": "density", "data": data, "axes_labels": {"xlabel": "X", "ylabel": "Y"}}
    multi.overlay(overlay_payload)

    multi()


.. image:: https://clidapp.s3.amazonaws.com/static/server/img/overlay_hetero_eg.jpg
    :alt: OverlayHeteroExample
    :align: center


Subplots
~~~~~~~~

The `new_subplot` method allows users to create a new subplot on the figure. The new_subplot method requires no arguments to be passed to the method. When a user is finished creating subplots, they can call the Multiplots object to render the figure.


.. code-block:: python

    import chartly

    # define main figure labels
    args = {"super_title": "Subplots Example", "super_xlabel": "X", "super_ylabel": "Y", "share_axes": False}

    multi = chartly.Multiplots(args)

    # Define Some Data
    data = np.random.normal(loc=0.8, scale=2, size=50)

    # Define Plots
    plots = ["histogram", "density", "probability_plot", "line_plot", "normal_cdf"]

    for plot in plots:
        # Create a subplot
        multi.new_subplot()
        axes_labels = {"xlabel": " ", "ylabel": " ", "title": plot}

        overlay_payload = {"plot": plot, "data": data, "axes_labels": axes_labels}
        multi.overlay(overlay_payload)

    multi.overlay(overlay_payload)

    multi()

.. image:: https://clidapp.s3.amazonaws.com/static/server/img/subplots_eg.jpg
    :alt: SubplotsExample
    :align: center

