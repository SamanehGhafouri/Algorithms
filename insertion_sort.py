
import unittest


def insertion_sort(items):
    return None

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






