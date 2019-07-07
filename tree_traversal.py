import unittest


class TreeNode:
    def __init__(self, value, left_child, right_child):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


three = TreeNode(3, None, None)
four = TreeNode(4, None, None)
two = TreeNode(2, three, four)
seven = TreeNode(7, None, None)
eight = TreeNode(8, None, None)
six = TreeNode(6, seven, eight)
nine = TreeNode(9, None, None)
five = TreeNode(5, six, nine)
one = TreeNode(1, two, five)


def pre_order_traversal(node, values):

    if node is None:
        return

    print(node.value)
    values.append(node.value)
    pre_order_traversal(node.left_child, values)
    pre_order_traversal(node.right_child, values)


class TestTreeTraversal(unittest.TestCase):

    def test_pre(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = []
        pre_order_traversal(one, actual)
        self.assertEqual(expected, actual, "Faild PreOrder")