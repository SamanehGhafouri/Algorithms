import unittest
import math


def merge_sort(items: list):
    pass


def merge(values, p_left_bound, q_mid_point, r_right_bound):
    pass

# writing 2 tests functions


class TestMergeSort(unittest.TestCase):

    def test_merge_of_nonempty_lists(self):

        items = [2, 3, 7, 8, 0, 1, 5, 9]
        expected = [0, 1, 2, 3, 5, 7, 8, 9]
        p = 0
        r = len(items)
        q = math.floor((p + r)/2)
        actual = merge(items, p, q, r)
        self.assertEqual(expected, actual, "Not merged, stupid.")

    def test_nonempty_even_list(self):
        items = [2, 8, 1, 5, 9, 3, 7, 11]
        expected = [1, 2, 3, 5, 7, 8, 9, 11]

        actual = merge_sort(items)
        self.assertEqual(expected, actual, "Not sorted")

    def test_nonempty_odd_list(self):
        items = [2, 8, 1, 5, 9, 3, 7]
        expected = [1, 2, 3, 5, 7, 8, 9]

        actual = merge_sort(items)
        self.assertEqual(expected, actual, "Not sorted")

    def test_empty_list(self):
        items = []
        expected = []

        actual = merge_sort(items)
        self.assertSequenceEqual(expected, actual, "Not sorted")


