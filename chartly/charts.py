"""Module to plot and customize various types of graphs.

:author: A.M.E. Popo[#]_,
    C.O. Mbengue[#]_,

:organization: Elizabeth Consulting International Inc.

This module contains the following classes:

    - :class:`LinePlot`: Class to plot a line plot.
    - :class:`CDF`: Class to plot a CDF plot.
    - :class:`Density`: Class to plot a density plot.
    - :class:`BoxPlot`: Class to plot a box plot.
    - :class:`Histogram`: Class to plot a histogram.
    - :class:`ProbabilityPlot`: Class to plot a probability plot.
    - :class:`Contour`: Class to plot a contour plot.
    - :class:`NormalCDF`: Class to plot a normal CDF plot.

.. [#] Azendae Marie-Ange Elizabeth Popo, Research Assistant, apopo@ec-intl.com
.. [#] Cheikh Oumar Mbengue, Research Scientist, cmbengue@ec-intl.com
.. [#] Elizabeth Consulting International Inc. (ECI) is a private company that
    specializes in the development of decision support systems for the
    private sector. ECI is based in St. Lucia, West Indies.
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
from matplotlib.ticker import MaxNLocator
from scipy.stats import norm

from .base import CustomizePlot, Plot


class LinePlot(Plot, CustomizePlot):
    """Class to plot a line plot.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: the data to plot

    Optional Keys
        - customs: the plot's customization
        - axes_labels: the axes labels

    Available Customizations
        - color: the color of the line plot, default is "navy"
        - linestyle: the style of the line plot, default is "solid"
    """

    def __init__(self, args):
        """Initialize the LinePlot Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def __call__(self):
        """Plot the line plot."""
        # Check if the data is 1D or 2D
        if isinstance(self.data[0], (list, np.ndarray)):
            # Check that both x and y data are present and of equal length
            assert len(self.data) == 2, "Data must contain both x and y list"
            assert len(self.data[0]) == len(self.data[1]), "Data lengths must be equal"
            data = self.data

        else:
            data = [self.data]

        self.ax.plot(
            *data,
            color=self.customs["color"],
            linewidth=1.5,
            linestyle=self.customs["linestyle"],
            label=self.axes_labels["linelabel"],
            marker=self.customs["marker"],
            ms=self.customs["markersize"],
            mec=self.customs["markeredgecolor"],
            mfc=self.customs["markercolor"],
        )
        self.label_axes()

    def defaults(self):
        """Set the default plot."""
        return {
            "color": "navy",
            "linestyle": "solid",
            "marker": "",
            "markersize": 5,
            "markercolor": "navy",
            "markeredgecolor": "navy",
        }


class ScatterPlot(Plot, CustomizePlot):
    """Class to plot a scatter plot.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: the data to plot

    Optional Keys
        - customs: the plot's customization
        - axes_labels: the axes labels

    Available Customizations
        - color: the color of the scatter plot, default is "navy"
        - marker: the marker style, default is "o"
        - size: the size of the markers, default is 5
        - edgecolor: the edge color of the markers, default is "navy"
        - alpha: the transparency of the markers, default is 1
    """

    def __init__(self, args):
        """Initialize the ScatterPlot Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def __call__(self):
        """Plot the scatter plot."""
        assert len(self.data) == 2 and isinstance(
            self.data[0], (list, np.ndarray)
        ), "Data must be 2D"

        self.ax.scatter(
            self.data[0],
            self.data[1],
            color=self.customs["color"],
            marker=self.customs["marker"],
            s=self.customs["size"],
            alpha=self.customs["alpha"],
            label=self.customs["label"],
        )

        self.label_axes()

    def defaults(self):
        """Set the default plot."""
        return {
            "color": "navy",
            "marker": "o",
            "size": 5,
            "alpha": 1,
            "label": " ",
        }


class CDF(Plot, CustomizePlot):
    """Class to plot a CDF plot.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: the data to plot

    Optional Keys
        - customs: the plot's customization

    Available Customizations
        - color: the color of the CDF plot, default is "dodgerblue"

    """

    def __init__(self, args):
        """Initialize the CDF Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        return {"color": "dodgerblue"}

    def __call__(self):
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
    """Class to plot a density plot.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: the data to plot

    Optional Keys
        - customs: the plot's customization

    Available Customizations
        - color: the color of the density plot, default is "red"
        - fill: whether to fill the density plot, default is False
        - label: the label of the density plot, default is " "
    """

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

    def __call__(self):
        """Plot the density plot."""
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
    """Class to plot a box plot.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: the data to plot

    Optional Keys
        - customs: the plot's customization
        - axes_labels: the axes labels

    Available Customizations
        - showfliers: whether to show the outliers, default is True
    """

    def __init__(self, args):
        """Initialize the BoxPlot Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        if isinstance(self.data[0], (list, np.ndarray)):
            label = [f"Dataset {i+1}" for i in range(len(self.data))]
        else:
            label = ["Dataset 1"]
        return {
            "showfliers": True,
            "boxlabels": label,
        }

    def __call__(self) -> None:
        """Plot Box Plots."""
        assert isinstance(
            self.data, (list, np.ndarray)
        ), "Data must be a list or a list of lists"
        assert isinstance(self.customs["boxlabels"], list), "Box labels must be a list"
        self.ax.boxplot(
            self.data,
            flierprops=dict(marker="o", markersize=1),
            medianprops=dict(color="red"),
            boxprops=dict(color="navy"),
            whiskerprops=dict(color="blue"),
            capprops=dict(color="red"),
            labels=self.customs["boxlabels"],
            showfliers=self.customs["showfliers"],
        )
        self.axes_labels["show_legend"] = False
        self.label_axes()


class Histogram(Plot, CustomizePlot):
    """Class to plot a histogram.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: the data to plot

    Optional Keys
        - customs: the plot's customization
        - axes_labels: the axes labels

    Available Customizations
        - num_bins: the number of bins in the histogram, default is 20
        - color: the color of the histogram, default is "plum"
        - ran: the range of the histogram, default is None
    """

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

    def __call__(self):
        """Plot a histogram"""
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
    """Class to plot a probability plot.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: the data to plot

    Optional Keys
        - customs: the plot's customization
        - axes_labels: the axes labels

    Available Customizations
        - color: the color of the scatter markers, default is "orangered"
    """

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

    def __call__(self):
        """Plot a probability plot."""
        # Extract Fields
        sample_data = self.data

        # Data Stats
        n = len(sample_data)

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
        sigma, mu = np.polyfit(z, sample_data, 1)

        # Plot Solid Line
        self.ax.axline(
            (0, mu),
            slope=sigma,
            color="black",
            linewidth=1,
            label=f"slope={sigma:.2f}, y-intercept={mu:.2f}",
        )

        # Create Axes Labels
        self.axes_labels.update({"xlabel": "z percentile", "ylabel": "Observations"})

        # label the axes
        self.label_axes()


class NormalCDF(Plot, CustomizePlot):
    """Class to plot a normal CDF plot.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: the data to plot

    Optional Keys
        - customs: the plot's customization
        - axes_labels: the axes labels

    """

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

    def __call__(self):
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
    """Class to plot a contour plot.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: a list of 2D numpy arrays

    Optional Keys
        - customs: the plot's customization
        - axes_labels: the axes labels

    Available Customizations
        - filled?: whether to fill the contour plot, default is False
        - colors: the color of the contour plot, default is "k"
        - inline?: whether to show the inline labels, default is True
        - fontsize: the font size of the labels, default is 9
        - colormap: the colormap of the contour plot, default is "viridis"
        - hatch?: whether to hatch the area, default is False
        - hatch_customs: the hatch customization, default is {}
    """

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
            "filled?": False,
            "colors": None,
            "labelcolor": "dimgray",
            "inline?": True,
            "fontsize": 9,
            "colormap": "viridis",
            "hatch?": False,
            "hatch_customs": {},
            "mask": None,
        }

        return def_dict

    def __call__(self):
        """Plot a contour plot."""
        func = self.ax.contourf if self.customs["filled?"] else self.ax.contour
        color = self.customs["colors"] if not self.customs["filled?"] else None

        assert len(self.data) == 3, "Contour plot requires 3 datasets"

        for data_ in self.data:
            assert data_.ndim == 2, "Data must be a 2D numpy array"

        CS = func(
            self.data[0],
            self.data[1],
            self.data[2],
            colors=color,
            cmap=self.customs["colormap"],
        )
        contour = CS

        if self.customs["filled?"]:
            dark_cmap = self.darker_cmap()
            edge_contours = self.ax.contour(
                self.data[0],
                self.data[1],
                self.data[2],
                cmap=dark_cmap,
                linewidths=0.5,
            )
            _ = self.fig.colorbar(
                CS, ax=self.ax, location="right", fraction=0.1, pad=0.02
            )
            contour = edge_contours

        self.ax.clabel(
            contour,
            fontsize=self.customs["fontsize"],
            inline=self.customs["inline?"],
            colors=self.customs["labelcolor"],
        )

        # Hatch the area
        if self.customs["hatch?"]:
            self.customs["hatch_customs"].update({"ax": self.ax})
            if self.customs["hatch_customs"]["type"] == "mask":
                self.customs["hatch_customs"]["data"] = [
                    self.data[0],
                    self.data[1],
                    self.customs["mask"],
                ]
            hatch = HatchArea(self.customs["hatch_customs"])
            hatch()

        self.axes_labels["show_legend"] = False
        self.label_axes()

    def darker_cmap(self, factor=0.7):
        """Make a colormap darker.

        :param str cmap: the colormap to darken
        :param float alpha: the transparency of the colormap
        """
        cmap = plt.get_cmap(self.customs["colormap"])
        colors = cmap(np.arange(cmap.N))
        dark_cmap = colors * factor
        dark_cmap[:, -1] = colors[:, -1]
        return LinearSegmentedColormap.from_list("darkened_cmap", dark_cmap)


class HatchArea(CustomizePlot):
    """Class to hatch the area between two points.

    :param dict args: the dictionary containing the customizations

    Required Keys
        - ax: the axis object

    Optional Keys
        - xy1: the first point
        - xy2: the second point
        - pattern: the hatch pattern
        - color: the color of the hatch
        - alpha: the transparency of the hatch
        - fill?: whether to fill the hatch or not
        - data: the data to use for the hatch"""

    def defaults(self):
        return {
            "xy1": (0, 0),
            "xy2": (1, 1),
            "pattern": "..",
            "color": "black",
            "alpha": 0.2,
            "fill?": False,
            "data": None,
            "type": "mask",
        }

    def __call__(self):
        """Hatch the area between two points.

        :param str func: the function to call. Either 'grid' or 'mask'

        Grid Required Keys
            - xy1: the first point
            - xy2: the second point

        Mask Required Keys
            - data: the data to use for the hatch
        """
        assert self.customs["type"] in ["grid", "mask"], "Invalid hatch type"
        if self.customs["type"] == "grid":
            x = self.customs["xy1"][0]
            y = self.customs["xy1"][1]
            width = self.customs["xy2"][0] - self.customs["xy1"][0]
            height = self.customs["xy2"][1] - self.customs["xy1"][1]

            self.customs["ax"].add_patch(
                Rectangle(
                    (x, y),
                    width,
                    height,
                    fill=self.customs["fill?"],
                    color=self.customs["color"],
                    alpha=self.customs["alpha"],
                    hatch=self.customs["pattern"],
                )
            )
        if self.customs["type"] == "mask":
            assert self.customs["data"] is not None, "Data must be provided"
            self.customs["ax"].contourf(
                self.customs["data"][0],
                self.customs["data"][1],
                self.customs["data"][2],
                [0.5, 1],
                hatches=[self.customs["pattern"]],
                alpha=self.customs["alpha"],
            )


class DotPlot(Plot, CustomizePlot):
    """Class to plot a dot plot.

    :param dict args: the master dictionary containing the required fields.

    Required Keys
        - data: the data to plot

    Optional Keys
        - customs: the plot's customization
        - axes_labels: the axes labels

    Available Customizations
        - color: the color of the dot plot, default is "black"
    """

    def __init__(self, args):
        """Initialize the DotPlot Class."""
        # Get the arguments
        self.args = args

        # Extract the customs
        customs_ = self.args.get("customs", {})
        super().__init__(self.args)
        CustomizePlot.__init__(self, customs_)

    def defaults(self):
        return {"color": "black", "bins": int(np.sqrt(len(self.data)))}

    def __call__(self):
        """Plot a dot plot"""
        assert isinstance(
            self.customs["bins"], (list, np.ndarray, int)
        ), "bins must be a sequence or an integer"
        # Define x and y lists
        x, y = [], []

        # Get the number of dots for each column
        if isinstance(self.customs["bins"], int):
            nbins = self.customs["bins"]

        elif isinstance(self.customs["bins"], (list, np.ndarray)):
            nbins = len(self.customs["bins"]) - 1

        counts, bins = np.histogram(self.data, bins=self.customs["bins"])

        # Create the x and y lists
        for i in range(nbins):
            x.extend([bins[i]] * counts[i])
            y.extend(range(1, counts[i] + 1))

        # Plot the dots
        self.ax.scatter(x, y, color=self.customs["color"])

        # Restrict the y ticks to only integers
        self.ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        # Set the x ticks to the bin edges
        self.ax.set_xticks(bins)

        # Set the x tick labels
        labels = [str(round(edge)) for edge in bins]
        self.ax.set_xticklabels(labels)

        # label the axes
        self.axes_labels["show_legend"] = False
        self.label_axes()
