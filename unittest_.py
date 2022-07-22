from copy import deepcopy
import unittest

from main import add


class AddTests(unittest.TestCase):

    """Tests for add."""

    def test_single_items(self):
        self.assertEqual(add([[5]], [[-2]]), [[3]])

    def test_two_by_two_matrixes(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4]]
        m3 = [[7, 8], [6, 5]]
        self.assertEqual(add(m1, m2), m3)

    def test_two_by_three_matrixes(self):
        m1 = [[1, 2, 3], [4, 5, 6]]
        m2 = [[-1, -2, -3], [-4, -5, -6]]
        m3 = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(add(m1, m2), m3)

    def test_input_unchanged(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4]]
        m1_original = deepcopy(m1)
        m2_original = deepcopy(m2)
        add(m1, m2)
        self.assertEqual(m1, m1_original)
        self.assertEqual(m2, m2_original)

    # To test bonus 1, comment out the next line
    @unittest.expectedFailure
    def test_any_number_of_matrixes(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4]]
        m3 = [[2, 1], [3, 4]]
        m4 = [[9, 9], [9, 9]]
        m5 = [[31, 32], [27, 24]]
        self.assertEqual(add(m1, m2, m3), m4)
        self.assertEqual(add(m2, m3, m1, m1, m2, m4, m1), m5)

    # To test bonus 2, comment out the next line
    @unittest.expectedFailure
    def test_different_matrix_size(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4], [5, 6]]
        m3 = [[6, 6], [3, 1, 2]]
        with self.assertRaises(ValueError):
            add(m1, m2)
        with self.assertRaises(ValueError):
            add(m1, m3)
        with self.assertRaises(ValueError):
            add(m1, m1, m1, m3, m1, m1)
        with self.assertRaises(ValueError):
            add(m1, m1, m1, m2, m1, m1)


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import python_version
    import sys
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2)