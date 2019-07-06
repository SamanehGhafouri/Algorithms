
import unittest


def insertion_sort(items):
    for j in range(1, len(items)):
        key = items[j]
        i = j - 1
        while i > -1 and items[i] > key:
            items[i + 1] = items[i]
            i = i - 1

        items[i + 1] = key

    return items

# writing the failing test. we need to pass nonempty input.


class TestInsertionSort(unittest.TestCase):

    def test_nonempty_input(self):
        items = [3, 8, 1, 0, 9]
        expected = [0, 1, 3, 8, 9]
        actual = insertion_sort(items)
        # assert is func that defines the unittest
        self.assertEqual(expected, actual, "Not sorted!")

    def test_empty_input(self):
        items = []
        expected = []
        actual = insertion_sort(items)
        self.assertEqual(expected, actual, "empty")






