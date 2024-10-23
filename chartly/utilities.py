"""Utilities module for the Chartly package."""
import math

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
