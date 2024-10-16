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
from scipy.stats import norm

color_list = ["slateblue", "lightpink", "skyblue", "plum", "mediumvioletred"]


class Plot:
    """
    Class that holds various methods used to plot graphs.

    :param dict args: the master dictionary containing both optional
        and required fields

    *Required Keys*
    - ax: an axis to plot the data
    - fig: the figure that the axis is on
    - data: a data list, or a list of data lists

    *Optional Keys*
    - axes_labels: the axes labels
    - boxplot_args: the optional customizations for a boxplot
    - cdf_args: the optional customizations for a cdf plot
    - hist_args: the optional customizations for a histogram
    - timeseries_args: the optional customizations for a timeseries plot
    - prob_plot_args: the optional customizations for a probability plot
    - gen_plot_args: the optional customizations for a generic plot
    - norm_cdf_args: the optional customizations for a normal cdf plot
    - contour_args: the optional customizations for a contour plot
    - density_args: the optional customizations for a density plot
    - export_args: the optional customizations for exporting the plot to a file

    **Examples**
    >>> fig, ax = plt.subplots()
    >>> data = [1, 2, 3, 4, 5]
    >>> args = {"ax": ax, "fig": fig, "data": data}
    >>> plot = Plot(args)
    >>> plot.data
    [1, 2, 3, 4, 5]
    """

    def __init__(self, args):
        """Initialize the Plot Class"""
        # Extract the data, axis, and figure
        self.data = args.get("data")
        self.ax = args.get("ax")
        self.fig = args.get("fig")

        # Initialize the Plot Utilities
        self.util = PlotUtilities()

        # Turn off interactive mode
        plt.ioff()

        # Extract axis labels
        self.axes_labels = {
            **self.set_defaults("axes_labels"),
            **args.get("axes_labels", {}),
        }

        # Extract Export Args
        self.export_args = {
            **self.set_defaults("export"),
            **args.get("export_args", {}),
        }

        # Extract Generic Plot Args
        self.gen_plot_args = {
            **self.set_defaults("gen_plot"),
            **args.get("gen_plot_args", {}),
        }

        # Extract boxplot Args
        self.boxplot_args = {
            **self.set_defaults("boxplots"),
            **args.get("boxplot_args", {}),
        }

        # Extract CDF Args
        self.cdf_args = {**self.set_defaults("cdf"), **args.get("cdf_args", {})}

        # Extract Density Plot Args
        self.density_args = {
            **self.set_defaults("density"),
            **args.get("density_args", {}),
        }
        args.get("density_args", self.set_defaults("density"))

        # Extract Histogram Args
        self.hist_args = {
            **self.set_defaults("histogram"),
            **args.get("histogram_args", {}),
        }

        # Extract Timeseries Args
        self.timeseries_args = {
            **self.set_defaults("timeseries"),
            **args.get("timeseries_args", {}),
        }
        # Extract Probability Plot Args
        self.prob_plot_args = {
            **self.set_defaults("prob_plot"),
            **args.get("prob_plot_args", {}),
        }

        # Extract Normal CDF Args
        self.norm_cdf_args = {
            **self.set_defaults("norm_cdf"),
            **args.get("norm_cdf_args", {}),
        }

        # Extract Contour Plot Args
        self.contour_args = {
            **self.set_defaults("contour"),
            **args.get("contour_args", {}),
        }

    def set_defaults(self, field):
        """Set Plot Class optional fields defaults

        :param str field: the field name
        :return: the plot default
        :rtype: dict
        """
        def_axes_labels = {
            "title": " ",
            "xlabel": " ",
            "ylabel": " ",
            "linelabel": " ",
            "boxlabel": " ",
            "show_legend": True,
            "scale": "linear",
            "base": 10,
        }
        def_contour = {
            "filled": False,
            "colors": "k",
            "inline": True,
            "fsize": 9,
        }

        defaults = {
            "axes_labels": def_axes_labels,
            "export": {"format": "eps", "fname": "plot.eps"},
            "cdf": {},
            "density": {"color": "red", "fill": False, "label": " "},
            "histogram": {"num_bins": 20, "color": "plum", "ran": None},
            "timeseries": {"linestyle": "solid", "color": "black"},
            "boxplots": {"showfliers": True},
            "prob_plot": {"color": "orangered"},
            "gen_plot": {"color": "navy", "linestyle": "solid"},
            "norm_cdf": {},
            "contour": def_contour,
        }
        return defaults[field]

    def update_defaults(self, field, new_values):
        """Update the optional fields default values.

        :param str field: the optional field to be updated
        :param dict values: the updated optional fields dict
        :rtype: None
        """

        defaults = {
            "axes_labels": self.axes_labels,
            "export": self.export_args,
            "cdf": self.cdf_args,
            "density": self.density_args,
            "histogram": self.hist_args,
            "timeseries": self.timeseries_args,
            "boxplots": self.boxplot_args,
            "prob_plot": self.prob_plot_args,
            "gen_plot": self.gen_plot_args,
            "norm_cdf": self.norm_cdf_args,
            "contour": self.contour_args,
        }

        defaults[field].update(new_values)

    def label_axes(self):
        """Label the axes of a graph. This method uses the axes_labels dict.
        There are no required keys for this dict.

        *Optional Keys*
        - xlabel: the x-axis label, default is " "
        - ylabel: the y-axis label, default is " "
        - title: the title of the graph, default is " "
        - linelabel: the label for the line, default is " "
        - show_legend: whether to show the legend or not, default is True
        - scale: the scale of the axes, default is "linear"
        - base: the base of the axes, default is 10

        """
        self.ax.set_title(self.axes_labels["title"])
        self.ax.set_xlabel(self.axes_labels["xlabel"])
        self.ax.set_ylabel(self.axes_labels["ylabel"])

        if self.axes_labels["scale"] in "semilogy loglog":
            plt.yscale("log", base=self.axes_labels["base"])

        if self.axes_labels["scale"] in "semilogx loglog":
            plt.xscale("log", base=self.axes_labels["base"])

        if self.axes_labels["show_legend"]:
            self.ax.legend()

    def generic_plot(self) -> None:
        """Plot a generic plot using y and/or x. This method uses the
        gen_plot_args dict. There are no required keys for this dict.

        *Optional Keys*
        - color: the color of the line, default is "navy"
        - linestyle: the style of the line, default is "solid"
        """
        # Check if the data is 1D or 2D
        if isinstance(self.data[0], (list, np.ndarray)):
            # Check that both x and y data are present and of equal length
            assert len(self.data) == 2, "Data must contain both x and y list"
            assert len(self.data[0]) == len(self.data[1]), "Data lengths must be equal"

            self.ax.plot(
                self.data[0],
                self.data[1],
                color=self.gen_plot_args["color"],
                linewidth=1.5,
                linestyle=self.gen_plot_args["linestyle"],
                label=self.axes_labels["linelabel"],
            )
        else:
            self.ax.plot(
                self.data,
                color=self.gen_plot_args["color"],
                linewidth=1.5,
                linestyle=self.gen_plot_args["linestyle"],
                label=self.axes_labels["linelabel"],
            )
        self.label_axes()

    def export_plot_to_file(self):
        """Export the current figure to a file. This method uses the export_args dict.
        There are no required keys for this dict.

        *Optional Keys*
        - format: the format of the exported file, default is "eps"
        - fname: the name of the exported file, default is "plot.eps"
        """

        self.fig.savefig(
            self.export_args["fname"],
            format=self.export_args["format"],
            bbox_inches="tight",
            pad_inches=1,
            orientation="portrait",
        )

    def plot_cdf(self) -> None:
        """Plot CDF of a dataset. This method uses the cdf_args dict. There are
        no required keys for this dict.
        """

        x = np.sort(self.data)
        y = np.cumsum(x) / np.sum(x)

        self.ax.plot(x, y, linewidth=1.5, label=self.axes_labels["linelabel"])

        for hline in (0.1, 0.5, 0.9):
            self.ax.axhline(y=hline, color="black", linewidth=1, linestyle="dashed")

        self.label_axes()

    def plot_density(self) -> None:
        """Plot the density plot of a dataset using kernel density estimation. This
        method uses the density_args dict. There are no required keys for this dict.

        *Optional Keys*
        - color: the color of the density plot, default is "red"
        - fill: whether to fill the density plot, default is False
        - label: the label of the density plot, default is " "
        """
        # Plot a density plot
        sns.kdeplot(
            self.data,
            color=self.density_args["color"],
            ax=self.ax,
            fill=self.density_args["fill"],
            label=self.density_args["label"],
        )
        self.label_axes()

    def plot_box_plots(self) -> None:
        """Plot Box Plots. This method uses the boxplot_args dict. There are no
        required keys for this dict.

        *Optional Keys*
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
            showfliers=self.boxplot_args["showfliers"],
        )
        self.axes_labels["show_legend"] = False
        self.label_axes()

    def plot_histogram(self):
        """Plot a histogram. This method uses the hist_args dict. There are no
        required keys for this dict.

        *Optional Keys*
        - num_bins: the number of bins in the histogram, default is 20
        - color: the color of the histogram, default is "plum"
        - ran: the range of the histogram, default is None
        """
        self.ax.hist(
            self.data,
            bins=self.hist_args["num_bins"],
            color=self.hist_args["color"],
            edgecolor="black",
            weights=np.ones_like(self.data) / len(self.data),
            range=self.hist_args["ran"],
        )
        self.axes_labels["show_legend"] = False
        self.label_axes()

    def plot_timeseries(self):
        """Plot a timeseries. This method uses the timeseries_args dict. There are no
        required keys for this dict.

        *Optional Keys*
        - linestyle: the style of the line, default is "solid"
        - color: the color of the line, default is "black"
        """
        self.ax.plot(
            self.data,
            linewidth=2,
            linestyle=self.timeseries_args["linestyle"],
            label=self.axes_labels["linelabel"],
            color=self.timeseries_args["color"],
        )
        self.label_axes()

    def plot_probability_plot(self):
        """Plot a probability plot. This method uses the prob_plot_args dict. There are no
        required keys for this dict.

        *Optional Keys*
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
            color=self.prob_plot_args["color"],
            s=30,
            marker="x",
        )

        # Plot Solid Line
        plt.axline((0, mu), slope=sigma, color="black", linewidth=1)

        # Create Axes Labels
        self.axes_labels.update(
            {
                "xlabel": "z percentile",
                "ylabel": "Observations",
                "show_legend": False,
            }
        )

        # label the axes
        self.label_axes()

    def plot_normal_cdf(self):
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

    def plot_contour_plot(self):
        """Plot a contour plot. This method uses the contour_args dict. There are no
        required keys for this dict. Please note that the data must be a list of
        2D numpy arrays.

        *Optional Keys*
        - filled: whether to fill the contour plot, default is False
        - colors: the color of the contour plot, default is "k"
        - inline: whether to show the inline labels, default is True
        - fsize: the font size of the labels, default is 9
        """
        func = self.ax.contourf if self.contour_args["filled"] else self.ax.contour

        assert len(self.data) == 3, "Contour plot requires 3 datasets"

        for data_ in self.data:
            assert data_.ndim == 2, "Data must be a 2D numpy array"

        CS = func(
            self.data[0],
            self.data[1],
            self.data[2],
            colors=self.contour_args["colors"],
        )
        self.ax.clabel(
            CS, fontsize=self.contour_args["fsize"], inline=self.contour_args["inline"]
        )
        self.axes_labels["show_legend"] = False
        self.label_axes()


class Multiplots(Plot):
    """Class to plot multiple subplots on the same graph.

    :param dict args: the master dictionary containing the required fields.

    *Required Keys*
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
        # Initialize the Plot Class
        super().__init__({"ax": "ax", "data": [], "fig": "fig"})

        # Extract Graph labels
        self.super_title = args.get("super_title", " ")
        self.super_xlabel = args.get("super_xlabel", " ")
        self.super_ylabel = args.get("super_ylabel", " ")
        self.share_axes = args.get("share_axes", True)

        # Turn off interactive mode
        plt.ioff()

        # Set the subplot count
        self.subplot_count = 0

        # Define the various graphing functions
        self.graphs = {
            "cdf": self.plot_cdf,
            "density": self.plot_density,
            "histogram": self.plot_histogram,
            "timeseries": self.plot_timeseries,
            "boxplots": self.plot_box_plots,
            "prob_plot": self.plot_probability_plot,
            "gen_plot": self.generic_plot,
            "contour": self.plot_contour_plot,
        }

        self.subplots = []
        self.current_subplot = []

    def overlay(self, overlay_args):
        """Overlay new plot onto current subplot.

        :param dict overlay_args: Master dictionary of all inputs

        *Required Keys*
        - plot: The graph name.
        - data: The data to plot onto the graph
        - axes_labels: The axes labels

        *Optional Keys*
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
                self.ax, self.data = ax, overlay[1]

                # Update the axes labels
                self.update_defaults("axes_labels", overlay[2])

                # Update the plot's defaults
                self.update_defaults(plot_name, overlay[3])

                # Plot the graph
                try:
                    self.graphs[plot_name]()
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


class PlotUtilities:
    """Class containing auxillary utility functions for plotting.

    **Usage**
    >>> util = PlottingUtilities()
    """

    def standardize_dataset(self, data: list) -> np.ndarray:
        """Standardize a dataset by subtracting the mean and dividing the std 
        of the dataset from each value.

        :param list data: the data list
        :return: standardized data
        :rtype: ndarray
        """
        # Convert the Data Into an array
        data = np.array(data)

        # Find the stats on the data
        mu = np.mean(data)
        sigma = np.std(data)

        # Return the standardized data
        return (data - mu) / sigma
