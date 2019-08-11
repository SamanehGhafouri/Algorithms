import unittest
import math


def find_max_crossing_subarray(items: list, low: int, mid: int, high: int) -> (int, int, int):

    max_left = -1
    max_right = -1

    left_sum = -999999999
    running_sum = 0
    for i in range(mid, low - 1,  -1):
        running_sum = running_sum + items[i]
        if running_sum > left_sum:
            left_sum = running_sum
            max_left = i

    right_sum = -999999999
    running_sum = 0
    for j in range(mid + 1, high):
        running_sum = running_sum + items[j]
        if running_sum > right_sum:
            right_sum = running_sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


class TestMaximumSubarraySolution(unittest.TestCase):

    def test_find_max_crossing_subarray_on_nonempty_list_one(self):

        items = [-5, 2, -1, 8, -3, 9, 5, -2]
        expected = (1, 6, 20)

        actual = find_max_crossing_subarray(items, 0, math.floor( (0 + 7)/2), 7)
        self.assertSequenceEqual(expected, actual)

    def test_find_max_crossing_subarray_on_nonempty_list_two(self):

        items = [-5, -1, 2, -8, -3, 9, 5, -2]
        expected = (2, 6, 5)

        actual = find_max_crossing_subarray(items, 0, math.floor( (0 + 7)/2), 7)
        self.assertSequenceEqual(expected, actual)
