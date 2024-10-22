"""Test plotting module.

:author: C.O. Mbengue [#]_,
    A.M.E. Popo [#]_

:organization: Elizabeth Consulting International Inc. [#]_

.. [#] Cheikh Oumar Mbengue, Research Scientist, cmbengue@ec-intl.com
.. [#] Azendae Marie-Ange Elizabeth Popo, Research Assistant, apopo@ec-intl.com
.. [#] Elizabeth Consulting International Inc. (ECI) is a private company that
    specializes in the development of decision support systems for the
    private sector. ECI is based in St. Lucia, West Indies.

"""

import unittest

import numpy as np
from chartly import Contour, LinePlot, Multiplots, PlotUtilities


class TestPlotting(unittest.TestCase):
    """Test the plotting module."""

    def setUp(self):
        """Set up the test class."""
        self.util = PlotUtilities()

        # Create a data list
        self.dataset_one = np.random.randint(50, size=(20))
        self.dataset_two = np.random.randint(50, size=(20))
        self.data = [self.dataset_one, self.dataset_two]

        # Create a dictionary of arguments
        self.args = {"display": False, "data": self.data}

        # Create a line plot object
        self.line_plot = LinePlot(self.args)

        # Create a contour plot object
        self.contour = Contour(self.args)

        # Create a dictionary of multiplot arguments
        args = {
            "super_title": " Test Title",
            "super_x_label": "Test X Label",
            "super_y_label": "Test Y Label",
        }
        # Create a multiplot object
        self.multiplot = Multiplots(args)

    def test_gen_plot_data_type(self):
        """Test that the generic plot can use both a 1D and 2D list of data."""
        # Test 1D data
        self.line_plot.data = self.dataset_one
        self.assertIsNone(self.line_plot.plot())

        # Test 2D data
        self.line_plot.data = self.data
        self.assertIsNone(self.line_plot.plot())

    def test_gen_plot_data_length(self):
        """Test that the generic plot throws an error if the data lengths are unequal."""
        self.line_plot.data = [self.dataset_one, self.dataset_two[:-1]]
        with self.assertRaises(AssertionError):
            self.line_plot.plot()

    def test_standardize_data(self):
        """Test that the data is standardized correctly."""
        data = [val for val in range(10, 100, 20)]
        expected_std_data = [-1.4, -0.7, 0, 0.7, 1.4]
        std_data = [np.round(val, 1) for val in self.util.standardize_dataset(data)]
        self.assertEqual(std_data, expected_std_data)

    def test_mutli_subplot_count(self):
        """Test that the multiplot object can handle multiple subplots."""
        # Test that initial subplot count is 0
        self.assertEqual(self.multiplot.subplot_count, 0)

        # Create a new subplot
        self.multiplot.new_subplot()

        # Test that the subplot count is now 1
        self.assertEqual(self.multiplot.subplot_count, 1)

        # Reset the subplot count
        self.multiplot.clear_axis()

    def test_multi_clear_axis(self):
        """Test that the multiplot object can clear the axis."""
        # Create a new subplot
        self.multiplot.new_subplot()

        # Test that the subplot count is now 1
        self.assertEqual(self.multiplot.subplot_count, 1)

        # Clear the axis
        self.multiplot.clear_axis()

        # Test that the subplot count is now 0
        self.assertEqual(self.multiplot.subplot_count, 0)

    def test_contour_data_length(self):
        """Test that the contour plot throws an error if the data lengths are unequal."""
        # Test that the contour plot throws an error when a user does not send 3 datasets
        self.contour.data = [self.dataset_one, self.dataset_two]
        with self.assertRaises(AssertionError):
            self.contour.plot()

        # test that the contour plot does not throw an error when a user sends 3 datasets
        X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
        Z = np.sin(X) * np.cos(Y)
        self.contour.data = [X, Y, Z]
        self.assertIsNone(self.contour.plot())

        # Test that the contour plot throws an error when the data sets are not 2D
        self.contour.data = [X, Y, Z[0]]
        with self.assertRaises(AssertionError):
            self.contour.plot()

    def test_default(self):
        """Test that the default plot is created correctly."""
        # Test that the default plot is created correctly
        customs = {"color": "pink"}
        args = {"data": self.data, "customs": customs, "display": False}
        plot_two = LinePlot(args)
        expect = {"color": "pink", "linestyle": "solid"}
        self.assertEqual(plot_two.customs, expect)


if __name__ == "__main__":
    unittest.main()
