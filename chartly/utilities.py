"""Utilities module for the Chartly package."""
import numpy as np


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
