Multiple Plot Charts with Chartly Examples
====================================

Chartly allows users to create multiple plots on the same figure using the `overlay` and `new_subplot` methods. The `overlay` method allows users to overlay multiple plots on a single subplot. The `new_subplot` method allows users to create a new subplot on the figure.


Overlay Plots
~~~~~~~~~~~~~

The `overlay` method allows users to overlay multiple plots on a single subplot. The overlay method requires a dictionary of arguments to be passed to the method. The dictionary should contain the following

- `data`: The data that will be plotted.
- `plot`: The type of plot to be created.

Users can also customize and label the plots by including the following keys in the dictionary:

- `axes_labels`: A dictionary containing the labels of the subplot.
- `customs`: A dictionary containing the customization options of the plot.

.. code-block:: python

    import chartly

    # define main figure labels
    args = {"super_title": "Overlay Example", "super_xlabel": "X", "super_ylabel": "Y", "share_axes": False}

    multi = chartly.Chart(args)

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

    multi()


.. image:: https://chartly.s3.amazonaws.com/static/server/img/overlay_hetero_eg.jpg
    :alt: OverlayHeteroExample
    :align: center


Subplots
~~~~~~~~

The `new_subplot` method allows users to create a new subplot on the figure. The new_subplot method requires no arguments to be passed to the method. When a user is finished creating subplots, they can call the Charts instance to render the figure.


.. code-block:: python

    import chartly

    # define main figure labels
    args = {"super_title": "Subplots Example", "super_xlabel": "X", "super_ylabel": "Y", "share_axes": False}

    multi = chartly.Chart(args)

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

.. image:: https://chartly.s3.amazonaws.com/static/server/img/subplots_eg.jpg
    :alt: SubplotsExample
    :align: center
