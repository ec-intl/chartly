"""Module to plot and customize various types of graphs.

:author: A.M.E. Popo[#]_,
    C.O. Mbengue[#]_,

:organization: Elizabeth Consulting International Inc.

This module contains the following classes:

    - :class:`Plot`: Class to plot various types of graphs.
    - :class:`PlotUtilities`: Class containing auxillary utility functions for plotting.
    - :class:`Multiplots`: Class to plot multiple subplots on the same graph.

.. [#] Azendae Marie-Ange Elizabeth Popo, Research Assistant, apopo@ec-intl.com
.. [#] Cheikh Oumar Mbengue, Research Scientist, cmbengue@ec-intl.com
.. [#] Elizabeth Consulting International Inc. (ECI) is a private company that
    specializes in the development of decision support systems for the
    private sector. ECI is based in St. Lucia, West Indies.
"""

import math

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.basemap import Basemap
from scipy.stats import norm

from .charts import CustomizePlot, HatchArea, Plot


class Multiplots(Plot):
    """Class to plot multiple subplots on the same graph.

    :param dict args: the master dictionary containing the required fields.

    Required Keys:
        - super_title: the title of the main figure
        - super_xlabel: the x-axis label of the main figure
        - super_ylabel: the y-axis label of the main figure
        - share_axes: whether to share the axes of the subplots

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

    def __init__(self, args):
        """Initialize the Multiplot Class."""
        # Turn off interactive mode
        plt.ioff()

        # Initialize the Plot Class
        super().__init__({"data": [], "display": False, "create_fig": False})

        # Extract Graph labels
        self.super_title = args.get("super_title", " ")
        self.super_xlabel = args.get("super_xlabel", " ")
        self.super_ylabel = args.get("super_ylabel", " ")
        self.share_axes = args.get("share_axes", True)

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
            "basemap": BaseMap,
        }

        self.subplots = []
        self.current_subplot = []

    def overlay(self, overlay_args):
        """Overlay new plot onto current subplot.

        :param dict overlay_args: Master dictionary of all inputs

        Required Keys:
            - plot: The graph name.
            - data: The data to plot onto the graph
            - axes_labels: The axes labels

        *Optional Keys*:
        customs: The plot's customization.
        """
        plot = overlay_args.get("plot")
        data = overlay_args.get("data")
        axes_labels = overlay_args.get("axes_labels")
        customs = overlay_args.get("customs", {})

        self.current_subplot.append([plot, data, axes_labels, customs])

    def new_subplot(self):
        """Create new subplot with current overlays"""
        # Increment the number of subplots already plotted
        self.subplot_count += 1
        if len(self.current_subplot) > 0:
            # Add all current overlays to a subplot
            self.subplots.append(self.current_subplot)

        # Reset current subplot
        self.current_subplot = []

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
        self.fig = plt.figure(figsize=(20, 8))
        rows, cols = self.tiling(self.subplot_count)
        ax1 = None

        # Add subplots
        for idx, subplot in enumerate(self.subplots):
            if idx == 0:
                ax = self.fig.add_subplot(rows, cols, idx + 1)
                ax1 = ax
            else:
                if self.share_axes:
                    ax = self.fig.add_subplot(rows, cols, idx + 1, sharey=ax1)
                else:
                    ax = self.fig.add_subplot(rows, cols, idx + 1)
            for overlay in subplot:
                plot_name = overlay[0]
                self.ax = ax

                # Prepare payload
                payload = {
                    "data": overlay[1],
                    "axes_labels": overlay[2],
                    "customs": overlay[3],
                    "display": False,
                    "create_fig": False,
                }

                # Plot the graph
                try:
                    plot = self.graphs[plot_name](payload)
                    plot.ax = self.ax
                    plot.plot()
                except Exception:
                    self.clear_axis()
                    raise

        # Add super titles
        self.fig.suptitle(self.super_title)
        self.fig.supxlabel(self.super_xlabel)
        self.fig.supylabel(self.super_ylabel)
        self.fig.tight_layout()
        plt.show()

        # Reset Canvas
        self.clear_axis()

    def clear_axis(self):
        """Reset Subplot Trackers."""
        self.subplot_count = 0
        self.subplots = []

    def tiling(self, num):
        """Calculates the number of rows and columns for the subplot.

        :param int num: the number of subplots
        :return: the number of rows and columns
        :rtype: tuple
        """
        if num < 5:
            return 1, num
        else:
            root = int(math.isqrt(num))
            if num == root**2:
                return root, root
            else:
                col = root + 1
                del_row = (col**2 - num) // col
                row = col - del_row
                return row, col


class LinePlot(Plot, CustomizePlot):
    """Class to plot a line plot."""

    def __init__(self, args):
        """Initialize the LinePlot Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def plot(self):
        """Plot the line plot."""
        # Check if the data is 1D or 2D
        if isinstance(self.data[0], (list, np.ndarray)):

            # Check that both x and y data are present and of equal length
            assert len(self.data) == 2, "Data must contain both x and y list"
            assert len(self.data[0]) == len(self.data[1]), "Data lengths must be equal"

            self.ax.plot(
                self.data[0],
                self.data[1],
                color=self.customs["color"],
                linewidth=1.5,
                linestyle=self.customs["linestyle"],
                label=self.axes_labels["linelabel"],
            )
        else:
            self.ax.plot(
                self.data,
                color=self.customs["color"],
                linewidth=1.5,
                linestyle=self.customs["linestyle"],
                label=self.axes_labels["linelabel"],
            )
        self.label_axes()

    def defaults(self):
        """Set the default plot."""
        return {"color": "navy", "linestyle": "solid"}


class CDF(Plot, CustomizePlot):
    """Class to plot a CDF plot."""

    def __init__(self, args):
        """Initialize the CDF Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        return {"color": "dogerblue"}

    def plot(self):
        """Plot the CDF."""

        x = np.sort(self.data)
        y = np.cumsum(x) / np.sum(x)

        self.ax.plot(
            x,
            y,
            linewidth=1.5,
            label=self.axes_labels["linelabel"],
            color=self.customs["color"],
        )

        for hline in (0.1, 0.5, 0.9):
            self.ax.axhline(y=hline, color="black", linewidth=1, linestyle="dashed")

        self.label_axes()


class Density(Plot, CustomizePlot):
    """Class to plot a density plot."""

    def __init__(self, args):
        """Initialize the Density Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        return {"color": "red", "fill": False, "label": " "}

    def plot(self):
        """Plot the density plot of a dataset using kernel density estimation. This
        method uses the density_args dict. There are no required keys for this dict.

        Optional Keys:
            - color: the color of the density plot, default is "red"
            - fill: whether to fill the density plot, default is False
            - label: the label of the density plot, default is " "
        """
        # Plot a density plot
        sns.kdeplot(
            self.data,
            color=self.customs["color"],
            ax=self.ax,
            fill=self.customs["fill"],
            label=self.customs["label"],
        )
        self.label_axes()


class BoxPlot(Plot, CustomizePlot):
    """Class to plot a box plot."""

    def __init__(self, args):
        """Initialize the BoxPlot Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        return {"showfliers": True}

    def plot(self) -> None:
        """Plot Box Plots. This method uses the boxplot_args dict. There are no
        required keys for this dict.

        Optional Keys:
            - showfliers: whether to show the outliers, default is True
        """

        self.ax.boxplot(
            self.data,
            flierprops=dict(marker="o", markersize=1),
            medianprops=dict(color="red"),
            boxprops=dict(color="navy"),
            whiskerprops=dict(color="blue"),
            capprops=dict(color="red"),
            tick_labels=self.axes_labels["boxlabel"],
            showfliers=self.customs["showfliers"],
        )
        self.axes_labels["show_legend"] = False
        self.label_axes()


class Histogram(Plot, CustomizePlot):
    """Class to plot a histogram."""

    def __init__(self, args):
        """Initialize the Histogram Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        return {"num_bins": 20, "color": "plum", "ran": None}

    def plot(self):
        """Plot a histogram. This method uses the hist_args dict. There are no
        required keys for this dict.

        Optional Keys:
            - num_bins: the number of bins in the histogram, default is 20
            - color: the color of the histogram, default is "plum"
            - ran: the range of the histogram, default is None
        """
        self.ax.hist(
            self.data,
            bins=self.customs["num_bins"],
            color=self.customs["color"],
            edgecolor="black",
            weights=np.ones_like(self.data) / len(self.data),
            range=self.customs["ran"],
        )
        self.axes_labels["show_legend"] = False
        self.label_axes()


class ProbabilityPlot(Plot, CustomizePlot):
    """Class to plot a probability plot."""

    def __init__(self, args):
        """Initialize the ProbabilityPlot Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        return {"color": "orangered"}

    def plot(self):
        """Plot a probability plot. This method uses the prob_plot_args dict.
        There are no required keys for this dict.

        Optional Keys:
            - color: the color of the plot, default is "orangered"
        """
        # Extract Fields
        sample_data = self.data

        # Data Stats
        n = len(sample_data)
        sigma = np.std(sample_data)
        mu = np.mean(sample_data)

        # Sort the data
        sample_data.sort()

        # Find percentiles
        pctls = [(i - 0.5) / n for i in range(1, n + 1)]

        # Find z percentiles
        z = [norm.ppf(pctl) for pctl in pctls]

        # Plot (z pctl, obs) ordered pairs
        self.ax.scatter(
            z,
            sample_data,
            color=self.customs["color"],
            s=30,
            marker="x",
        )

        # Plot Solid Line
        self.ax.axline(
            (0, mu),
            slope=sigma,
            color="black",
            linewidth=1,
            label=f"slope={mu:.2f}, y-intercept={sigma:.2f}",
        )

        # Create Axes Labels
        self.axes_labels.update({"xlabel": "z percentile", "ylabel": "Observations"})

        # label the axes
        self.label_axes()


class NormalCDF(Plot, CustomizePlot):
    """Class to plot a normal CDF plot."""

    def __init__(self, args):
        """Initialize the NormalCDF Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        return {"color": "green"}

    def plot(self):
        """Plot a standard normal distribution CDF against the CDF
        of other datasets. This method uses the norm_cdf_args dict. There are no
        required keys for this dict.
        """
        data_list = (
            self.data if isinstance(self.data[0], (list, np.ndarray)) else [self.data]
        )

        for idx, data in enumerate(data_list):
            # Standardize the data
            x = np.sort(self.util.standardize_dataset(data))
            n = len(x)

            # Find the percentiles
            pctls = [(i - 0.5) / n for i in range(1, n + 1)]

            # Plot Sample CDF
            self.ax.plot(
                x,
                pctls,
                linewidth=1.5,
                linestyle="solid",
                label=f"Sample Dataset {idx + 1} CDF",
            )

        # Find the z values
        z = np.linspace(-3.4, 3.4)

        # Find the p values
        p_vals = [norm.cdf(z_) for z_ in z]

        # Plot Stanfard Normal CDF
        self.ax.plot(
            z,
            p_vals,
            linewidth=1.5,
            linestyle="dashed",
            label="Standard Normal CDF",
            color="red",
        )

        # label the axes
        self.label_axes()


class Contour(Plot, CustomizePlot):
    """Class to plot a contour plot."""

    def __init__(self, args):
        """Initialize the Contour Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        def_dict = {
            "filled": False,
            "colors": None,
            "inline": True,
            "fsize": 9,
            "cmap": "viridis",
            "hatch": False,
            "hatch_color": "black",
            "hatch_alpha": 0,
            "hatch_fill": True,
            "pattern": "..",
            "xy1": (0, 0),
            "xy2": (1, 1),
            "hatch_grid": False,
            "hatch_mask": False,
            "mask": None,
        }
        return def_dict

    def plot(self):
        """Plot a contour plot. This method uses the contour_args dict. There are no
        required keys for this dict. Please note that the data must be a list of
        2D numpy arrays.

        Optional Keys:
            - filled: whether to fill the contour plot, default is False
            - colors: the color of the contour plot, default is "k"
            - inline: whether to show the inline labels, default is True
            - fsize: the font size of the labels, default is 9
        """
        func = self.ax.contourf if self.customs["filled"] else self.ax.contour
        color = (
            self.customs["colors"]
            if not self.customs["filled"]
            else None
        )

        assert len(self.data) == 3, "Contour plot requires 3 datasets"

        for data_ in self.data:
            assert data_.ndim == 2, "Data must be a 2D numpy array"

        CS = func(
            self.data[0],
            self.data[1],
            self.data[2],
            colors=color,
            cmap=self.customs["cmap"],
        )
        self.ax.clabel(
            CS,
            fontsize=self.customs["fsize"],
            inline=self.customs["inline"],
        )

        if self.customs["hatch_grid"] or self.customs["hatch_mask"]:
            payload = {
                "ax": self.ax,
                "pattern": self.customs["pattern"],
                "color": self.customs["hatch_color"],
                "alpha": self.customs["hatch_alpha"],
                "fill": self.customs["hatch_fill"],
            }
            if self.customs["hatch_grid"]:
                payload.update(
                    {
                        "ax": self.ax,
                        "xy1": self.customs["xy1"],
                        "xy2": self.customs["xy2"],
                    }
                )
                hatch = HatchArea(payload)
                hatch("grid")
            if self.customs["hatch_mask"]:
                payload.update(
                    {
                        "data": [
                            self.data[0],
                            self.data[1],
                            self.customs["mask"],
                        ],
                    }
                )
                hatch = HatchArea(payload)
                hatch("mask")
        self.axes_labels["show_legend"] = False
        self.label_axes()


class BaseMap(Plot, CustomizePlot):
    """Class to plot a basemap plot."""

    def __init__(self, args):
        """Initialize the BasemapPlot Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        """Set the default plot."""
        return {
            "proj": "ortho",
            "draw_coastlines": True,
            "fillcontinents": False,
            "draw_countries": False,
            "draw_states": False,
            "draw_rivers": False,
            "bluemarble": False,
            "shaderelief": False,
            "draw_parallels": False,
            "draw_meridians": False,
        }

    def plot(self):
        """plot a basemap plot

        Customs:
            - proj: the projection of the map, default is "ortho"
            - draw_coastlines: whether to draw coastlines, default is True
            - fillcontinents: whether to fill continents, default is False
            - draw_countries: whether to draw countries, default is False
            - draw_states: whether to draw states, default is False
            - draw_rivers: whether to draw rivers, default is False
            - bluemarble: whether to use the bluemarble map, default is False
            - shaderelief: whether to use the shaded relief map, default is False
            - draw_parallels: whether to draw parallels, default is False
            - draw_meridians: whether to draw meridians, default is False
        """
        map_ = Basemap(projection=self.customs["proj"], lat_0=0, lon_0=0)

        basemap_methods = {
            "draw_coastlines": map_.drawcoastlines,
            "fillcontinents": map_.fillcontinents,
            "draw_countries": map_.drawcountries,
            "draw_states": map_.drawstates,
            "draw_rivers": map_.drawrivers,
            "bluemarble": map_.bluemarble,
            "shaderelief": map_.shadedrelief,
            "draw_parallels": lambda: map_.drawparallels(np.arange(-90, 90, 30)),
            "draw_meridians": lambda: map_.drawmeridians(np.arange(0, 360, 60)),
        }

        for key, method in basemap_methods.items():
            if self.customs.get(key):
                method()

        self.axes_labels["show_legend"] = False
        self.label_axes()
