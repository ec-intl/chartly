Multiple Plot Charts with Chartly Examples
==========================================

Chartly allows users to create multiple plots on the same figure using the `overlay` and `new_subplot` methods. The `overlay` method allows users to overlay multiple plots on a single subplot. The `new_subplot` method allows users to create a new subplot on the figure.


Overlay Plots
~~~~~~~~~~~~~

To overlay multiple plots on a single subplot, first add the subplot with
``add_subplot(...)`` and then add additional plots to that same subplot with
``add_overlay(...)``.

.. code-block:: python

    import chartly
    import numpy as np

    # define main figure labels
    args = {
        "super_title": "Overlay Example",
        "super_xlabel": "X",
        "super_ylabel": "Y",
        "share_axes": False,
    }

    multi = chartly.Chart(args)

    # Define Some Data
    data = np.random.normal(loc=2, scale=1, size=1000)

    # Add a subplot and overlay a second plot
    multi.add_subplot("histogram", data)
    multi.add_overlay("density", data)

    multi.render()


.. image:: https://chartly.s3.amazonaws.com/static/img/overlay_hetero_eg.jpg
    :alt: OverlayHeteroExample
    :align: center
    :height: 500px


Subplots
~~~~~~~~

To create multiple subplots on the same figure, add each subplot directly
with ``add_subplot(...)`` and render the figure with ``render()`` once all
subplots have been added.

.. code-block:: python

    import chartly
    import numpy as np

    # define main figure labels
    args = {
        "super_title": "Subplots Example",
        "super_xlabel": "X",
        "super_ylabel": "Y",
        "share_axes": False,
    }

    multi = chartly.Chart(args)

    # Define Some Data
    data = np.random.normal(loc=0.8, scale=2, size=50)

    # Add subplots directly
    multi.add_subplot("histogram", data, axes_labels={"title": "histogram"})
    multi.add_subplot("density", data, axes_labels={"title": "density"})
    multi.add_subplot(
        "probability_plot",
        data,
        axes_labels={"title": "probability_plot"},
    )
    multi.add_subplot("line_plot", data, axes_labels={"title": "line_plot"})
    multi.add_subplot("normal_cdf", data, axes_labels={"title": "normal_cdf"})

    multi.render()

.. image:: https://chartly.s3.amazonaws.com/static/img/subplots_eg.jpg
    :alt: SubplotsExample
    :align: center
    :height: 500px
