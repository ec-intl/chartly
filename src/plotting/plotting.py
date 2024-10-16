"""Visualization Module"""

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

    **Required Keys**
    - ax: an axis to plot the data
    - fig: the figure that the axis is on
    - data: a data list

    **Optional Keys**
    - axes_labels: the axes labels
    - boxplot_args: the optional customizations for a boxplot
    - cdf_args: the optional customizations for a cdf plot
    - hist_args: the optional customizations for a histogram
    - timeseries_args: the optional customizations for a timeseries plot

    **Usage**
    >>> _, ax = plt.subplots()
    >>> data = np.random.randint(50, size=(20))
    >>> args = {"ax": ax, "data": data}
    >>> plot = Plot(args)
    """

    def __init__(self, args):
        """Initialize Plot Class"""

        self.data = args.get("data")
        self.ax = args.get("ax")
        self.fig = args.get("fig")

        self.util = PlottingUtilities()

        # Turn off interactive mode
        plt.ioff()

        # Extract axis labels
        self.axes_labels = args.get("axes_labels", self.set_defaults("axes_labels"))

        # Extract Export Args
        self.export_args = args.get("export_args", self.set_defaults("export"))

        # Extract Generic Plot Args
        self.gen_plot_args = args.get("gen_plot_args", self.set_defaults("gen_plot"))

        # Extract boxplot Args
        self.boxplot_args = args.get("boxplot_args", self.set_defaults("boxplots"))

        # Extract CDF Args
        self.cdf_args = args.get("cdf_args", self.set_defaults("cdf"))

        # Extract Density Plot Args
        self.density_args = args.get("density_args", self.set_defaults("density"))

        # Extract Histogram Args
        self.hist_args = args.get("hist_args", self.set_defaults("histogram"))

        # Extract Timeseries Args
        self.timeseries_args = args.get(
            "timeseries_args", self.set_defaults("timeseries")
        )

        # Extract Probability Plot Args
        self.prob_plot_args = args.get("prob_plot_args", self.set_defaults("prob_plot"))

        # Extract Normal CDF Args
        self.norm_cdf_args = args.get("norm_cdf_args", self.set_defaults("norm_cdf"))

        # Extract Contour Plot Args
        self.contour_args = args.get("contour_args", self.set_defaults("contour"))

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
            "cdf": {"logxscale": False},
            "density": {"color": "red", "fill": False, "label": " "},
            "histogram": {"num_bins": 20, "color": "plum", "ran": None},
            "timeseries": {"linestyle": "solid", "color": "black"},
            "boxplots": {"showfliers": True},
            "prob_plot": {"color": "orangered"},
            "gen_plot": {"color": "navy", "linestyle": "solid"},
            "norm_cdf": {"add_datasets": []},
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
        """Label the axes of a graph.

        :param ax: the axis.
        :param dict axes_labels: Dict of the labels for each axes. These include
            xlabel, ylabel, and title.
        :param bool legend: whether to show the legend or not.
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
        """Generic Plot"""
        if isinstance(self.data[0], (list, np.ndarray)):
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
        """Export the current figure to a file."""

        self.fig.savefig(
            self.export_args["fname"],
            format=self.export_args["format"],
            bbox_inches="tight",
            pad_inches=1,
            orientation="portrait",
        )

    def plot_cdf(self) -> None:
        """Plot CDF of a dataset."""

        x = np.sort(self.data)
        y = np.cumsum(x) / np.sum(x)

        self.ax.plot(x, y, linewidth=1.5, label=self.axes_labels["linelabel"])

        for hline in (0.1, 0.5, 0.9):
            self.ax.axhline(y=hline, color="black", linewidth=1, linestyle="dashed")

        self.label_axes()

    def plot_density(self) -> None:
        """Plot the density plot of a dataset using kernel density estimation"""
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
        """Plot Box Plots."""

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
        """Plot histogram."""
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
        """Plot timeseries"""
        self.ax.plot(
            self.data,
            linewidth=2,
            linestyle=self.timeseries_args["linestyle"],
            label=self.axes_labels["linelabel"],
            color=self.timeseries_args["color"],
        )
        self.label_axes()

    def plot_probability_plot(self):
        """Plot probability plot"""
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
        of other datasets."""
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
        """Plot a contour plot"""
        func = self.ax.contourf if self.contour_args["filled"] else self.ax.contour

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

    **Usage**
    >>> multiplot = Multiplots()
    """

    def __init__(self, args):
        """Initialize multiplot class."""
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
        """Overlay new plot onto subplot.

        :param dict overlay_args: Master dictionary of all inputs

        **Required Keys**
        - plot: The graph name.
        - data: The data to plot onto the graph
        - axes_labels: The axes labels

        **Optional Keys**
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

        :param dict super_axes_labels: dict of all the main figure's labels
        **Required Keys**
        - title
        - xlabel
        - ylabel
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
                self.graphs[plot_name]()

        # Add super titles
        self.fig.suptitle(self.super_title)
        self.fig.supxlabel(self.super_xlabel)
        self.fig.supylabel(self.super_ylabel)
        self.fig.tight_layout()
        plt.show()

        # Reset Canvas
        self.clear_axis()

    def clear_axis(self):
        """Reset Subplot Trackers"""
        self.subplot_count = 0
        self.subplots = []

    def tiling(self, num):
        """Calculates the number of rows and columns for the subplot.

        :param int num: the number of subplots
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


class PlottingUtilities:
    """Class containing auxillary utility functions for plotting.

    **Usage**
    >>> util = PlottingUtilities()
    """

    def standardize_dataset(self, data: list) -> np.ndarray:
        """Standardize a dataset.

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
