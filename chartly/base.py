from abc import ABC, abstractmethod

import matplotlib.pyplot as plt

from .utilities import PlotUtilities


class Plot:
    """
    Base Class for Chartly's Plots. This class handles setting up and labelling
    the axes of a plot.

    :param dict args: the master dictionary containing both optional
        and required fields

    Required Keys
        - data: a data list, or a list of data lists

    Optional Keys
        - axes_labels (dict): the axes labels
        - display (bool): whether to display the plot or not. Default is True

    **Examples**

    >>> data = [1, 2, 3, 4, 5]
    >>> args = {"data": data}
    >>> plot = Plot(args)
    >>> plot.data
    [1, 2, 3, 4, 5]
    """

    _fig, _ax = None, None

    def __init__(self, args):
        """Initialize the Plot Class"""
        self.args = args

        # Extract the data
        self.data = self.args.get("data")

        self.display = self.args.get("display", True)

        # Set the filename and format
        self._last_fig = Plot._fig
        self._fname = "plot"
        self._format = "eps"

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

        # Extract axis labels
        self.axes_labels = {
            **def_axes_labels,
            **self.args.get("axes_labels", {}),
        }

        # Initialize the Plot Utilities
        self.util = PlotUtilities()

    @property
    def fig(self):
        """Get the figure."""
        self.create_plot()
        return Plot._fig

    @fig.setter
    def fig(self, value):
        Plot._fig = value

    @property
    def ax(self):
        """Get the figure."""
        self.create_plot()
        return Plot._ax

    @ax.setter
    def ax(self, value):
        Plot._ax = value

    @property
    def fname(self):
        """Get the figure."""
        return self._fname

    @fname.setter
    def fname(self, value):
        self._fname = value

    @property
    def format(self):
        """Get the figure."""
        return self._format

    @format.setter
    def format(self, value):
        self._format = value

    @property
    def last_fig(self):
        """Get the last figure."""
        return self._last_fig

    @last_fig.setter
    def last_fig(self, value):
        self._last_fig = value

    def create_plot(self):
        """Create a plot."""
        if Plot._fig is None or Plot._ax is None:
            Plot._fig, Plot._ax = plt.subplots()

    def clear_plot(self):
        """Clear the plot."""
        Plot._fig, Plot._ax = None, None

    def label_axes(self):
        """Label the axes of a graph. This method uses the axes_labels dict.
        There are no required keys for this dict.

        Optional Keys
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

        if self.display:
            self.display_plot()
        else:
            self._last_fig = self.fig

    def display_plot(self):
        """Display the plot."""
        plt.show()
        self._last_fig = self.fig
        self.clear_plot()

    def save(self):
        """Export the current figure to a file. The default filename is 'plot'
        and the default format is 'eps'.
        """

        self.last_fig.savefig(
            f"{self.fname}.{self.format}",
            format=self.format,
            bbox_inches="tight",
            pad_inches=1,
            orientation="portrait",
        )


class CustomizePlot(ABC):
    """Class to customize the appearance of a map."""

    def __init__(self, customs):
        """Initialize the CustomizeMap Class.

        :param dict customs: the dictionary containing the customizations
        """
        self.config = self.defaults()
        self._customs = customs

    @abstractmethod
    def defaults(self):
        """Set the default plot."""
        pass

    @abstractmethod
    def __call__(self):
        """Plot the graph."""
        pass

    @property
    def customs(self):
        """Get the customs."""
        self.config.update(self._customs)
        return self.config
