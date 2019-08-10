import unittest
import math


def merge_sort(a, p, r):

    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)


def merge(a, p, q, r):

    list_left =[]
    list_right =[]
    for i in range(p, q + 1):
        list_left.append(a[i])
    for j in range(q + 1, r + 1):
        list_right.append(a[j])

    list_left.append(99999999)
    list_right.append(999999999)

    i, j = 0, 0
    for k in range(p, r + 1):
        if list_left[i] <= list_right[j]:
            a[k] = list_left[i]
            i = i + 1
        else:
            a[k] = list_right[j]
            j = j + 1

# writing 2 tests function


class TestMergeSort(unittest.TestCase):

    def test_merge_of_nonempty_lists(self):

        items = [7, 8, 2, 3]
        expected = [2, 3, 7, 8]
        p = 0
        r = 3
        q = math.floor((p + r)/2)
        merge(items, p, q, r)
        self.assertEqual(expected, items, "Not merged, stupid.")

    def test_nonempty_even_list(self):
        items = [2, 8, 1, 5, 9, 3, 7, 11]
        expected = [1, 2, 3, 5, 7, 8, 9, 11]

        merge_sort(items, 0, 7)
        self.assertEqual(expected, items, "Not sorted")
    #
    # def test_nonempty_odd_list(self):
    #     items = [2, 8, 1, 5, 9, 3, 7]
    #     expected = [1, 2, 3, 5, 7, 8, 9]
    #
    #     actual = merge_sort(items)
    #     self.assertEqual(expected, actual, "Not sorted")
    #
    # def test_empty_list(self):
    #     items = []
    #     expected = []
    #
    #     actual = merge_sort(items)
    #     self.assertSequenceEqual(expected, actual, "Not sorted")


