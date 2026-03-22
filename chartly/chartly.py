"""Module to plot and customize various types of graphs.

:author: A.M.E. Popo[#]_,
    C.O. Mbengue[#]_,

:organization: Elizabeth Consulting International Inc.

This module contains the following classes:

    - :class:`Chart`: Class to plot multiple subplots on the same graph.

.. [#] Azendae Marie-Ange Elizabeth Popo, Research Assistant, apopo@ec-intl.com
.. [#] Cheikh Oumar Mbengue, Research Scientist, cmbengue@ec-intl.com
.. [#] Elizabeth Consulting International Inc. (ECI) is a private company that
    specializes in the development of decision support systems for the
    private sector. ECI is based in St. Lucia, West Indies.
"""

import matplotlib.pyplot as plt

from .base import Plot
from .charts import (
    CDF,
    Basemap,
    BoxPlot,
    Contour,
    Density,
    DotPlot,
    Histogram,
    LinePlot,
    NormalCDF,
    ProbabilityPlot,
    ScatterPlot,
    bmap,
)


# pylint: disable=too-many-instance-attributes,too-many-branches
class Chart(Plot):
    """Class to plot multiple subplots on the same graph.

    :param dict args: the master dictionary containing the required fields.

    Required Keys:
        - super_title: the title of the main figure
        - super_xlabel: the x-axis label of the main figure
        - super_ylabel: the y-axis label of the main figure
        - share_axes: whether to share the axes of the subplots
        - show: whether to display the main figure or not. Default is True

    **Example**

    >>> args = {
    ...     "super_title": "Test Title",
    ...     "super_xlabel": "Test X Label",
    ...     "super_ylabel": "Test Y Label",
    ...     "share_axes": False,
    ... }
    >>> multiplot = Multiplots(args)
    >>> multiplot.share_axes
    False
    """

    def __init__(self, args=None):
        """Initialize the Multiplot Class."""
        args = {} if args is None else args

        # Turn off interactive mode
        plt.ioff()

        # Initialize the Plot Class
        super().__init__({"data": [], "display": False})

        # Extract Graph labels
        self.super_title = args.get("super_title", "")
        self.super_xlabel = args.get("super_xlabel", "")
        self.super_ylabel = args.get("super_ylabel", "")
        self.share_axes = args.get("share_axes", True)
        self.show = args.get("show", True)

        # Set the subplot count
        self.subplot_count = 0

        # Define the various graphing functions
        self.graphs = {
            "cdf": CDF,
            "density": Density,
            "histogram": Histogram,
            "boxplot": BoxPlot,
            "probability_plot": ProbabilityPlot,
            "line_plot": LinePlot,
            "contour": Contour,
            "normal_cdf": NormalCDF,
            "basemap": Basemap,
            "scatter": ScatterPlot,
            "dotplot": DotPlot,
        }

        self.subplots = []
        self.current_subplot = []

    def overlay(self, overlay_args):
        """Overlay new plot onto current subplot.

        :param dict overlay_args: Master dictionary of all inputs

        Required Keys:
            - plot: The graph name.
            - data: The data to plot onto the graph

        Optional Keys:
            - axes_labels: The axes labels for the subplot.
            - customs: The plot's customization.
        """
        plot = overlay_args.get("plot")
        data = overlay_args.get("data")
        axes_labels = overlay_args.get("axes_labels", {})
        customs = overlay_args.get("customs", {})

        self.current_subplot.append([plot, data, axes_labels, customs])

    def new_subplot(self, args=None):
        """Create new subplot with current overlays

        :param dict args: Optional. Master dictionary of all inputs to plot a graph.

        Required Keys:
            - plot: The graph name.
            - data: The data to plot onto the graph

        Optional Keys:
            - axes_labels: The axes labels for the subplot.
            - customs: The plot's customization.
        """
        args = {} if args is None else args

        # Increment the number of subplots already plotted
        self.subplot_count += 1
        if len(self.current_subplot) > 0:
            # Add all current overlays to a subplot
            self.subplots.append(self.current_subplot)

        # Reset current subplot
        self.current_subplot = []
        if args:
            self.overlay(args)

    def render(self):
        """Render the chart."""
        return self()

    def add_subplot(self, plot, data, axes_labels=None, customs=None):
        """Add a new subplot with a single plot."""
        axes_labels = {} if axes_labels is None else axes_labels
        customs = {} if customs is None else customs

        self.new_subplot(
            {
                "plot": plot,
                "data": data,
                "axes_labels": axes_labels,
                "customs": customs,
            }
        )

    def add_overlay(self, plot, data, axes_labels=None, customs=None):
        """Overlay a plot onto the current subplot."""
        axes_labels = {} if axes_labels is None else axes_labels
        customs = {} if customs is None else customs

        self.overlay(
            {
                "plot": plot,
                "data": data,
                "axes_labels": axes_labels,
                "customs": customs,
            }
        )

    def add_basemap(self, lon, lat, values, customs=None):
        """Add a basemap subplot from raw longitude, latitude, and value grids."""
        customs = {} if customs is None else customs

        map_projection = bmap(
            projection=customs.get("proj", "ortho"),
            lat_0=customs.get("lat_0", 0),
            lon_0=customs.get("lon_0", 0),
        )

        lon_shifted, values_shifted = map_projection.shiftdata(
            lon,
            datain=values,
            lon_0=customs.get("lon_0", 0),
        )
        x, y = map_projection(lon_shifted, lat)

        basemap_customs = dict(customs)
        basemap_customs["proj"] = customs.get("proj", "ortho")

        self.add_subplot(
            "basemap",
            [x, y, values_shifted],
            customs=basemap_customs,
        )

    def __call__(self):
        """Build the main figure, label its axes and display the result.

        **Usage**

        >>> args = {
        ...     "super_title": "Test Title",
        ...     "super_xlabel": "Test X Label",
        ...     "super_ylabel": "Test Y Label",
        ...     "share_axes": False,
        ... }
        >>> multiplot = Multiplots(args)
        >>> multiplot.new_subplot()
        >>> overlay_args = {
        ...     "plot": "cdf",
        ...     "data": [1, 2, 3, 4, 5],
        ...     "axes_labels": {"title": "CDF Plot", "xlabel": "X", "ylabel": "Y"},
        ... }
        >>> multiplot.overlay(overlay_args)
        >>> multiplot()
        """
        # Collect and Store remaining overlays
        self.subplots.append(self.current_subplot)
        # reset current overlay
        self.current_subplot = []

        # Set Up the Figure and Num of Rows and Columns
        Plot._fig = plt.figure(figsize=(20, 8))
        rows, cols = self.util.tiling(self.subplot_count)
        ax1 = None
        has_basemap = False

        # Add subplots
        for idx, subplot in enumerate(self.subplots):
            if idx == 0:
                ax = Plot._fig.add_subplot(rows, cols, idx + 1)
                ax1 = ax
            else:
                if self.share_axes:
                    ax = Plot._fig.add_subplot(rows, cols, idx + 1, sharey=ax1)
                else:
                    ax = Plot._fig.add_subplot(rows, cols, idx + 1)

            subplot_has_basemap = any(overlay[0] == "basemap" for overlay in subplot)

            for overlay in subplot:
                plot_name = overlay[0]
                if plot_name == "basemap":
                    has_basemap = True
                Plot._ax = ax

                # Prepare payload
                payload = {
                    "data": overlay[1],
                    "axes_labels": overlay[2],
                    "customs": overlay[3],
                    "display": False,
                }

                # Plot the graph
                try:
                    plot = self.graphs[plot_name](payload)
                    plot.ax = self.ax
                    plot()
                except Exception:
                    self.clear_axis()
                    raise

            if subplot_has_basemap:
                ax.set_anchor("C")
                ax.set_aspect("equal", adjustable="box")

        # Add super titles
        if self.super_title.strip():
            self.fig.suptitle(self.super_title)

        if self.super_xlabel.strip():
            self.fig.supxlabel(self.super_xlabel)

        if self.super_ylabel.strip():
            self.fig.supylabel(self.super_ylabel)

        if has_basemap:
            self.fig.subplots_adjust(left=0.12, right=0.88, top=0.88, bottom=0.12)
        else:
            self.fig.tight_layout()

        if self.show:
            self.display_plot()

        else:
            self._last_fig = Plot._fig
            self.clear_plot()
            plt.close()

        # Reset Canvas
        self.clear_axis()

    def clear_axis(self):
        """Reset Subplot Trackers."""
        self.subplot_count = 0
        self.subplots = []
