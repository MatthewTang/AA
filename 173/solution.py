import unittest
from typing import List, Optional
from Tree.solution import TreeNode


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        in_order = []

        def dfs(curr: Optional[TreeNode]):
            if curr is None:
                return
            dfs(curr.left)
            in_order.append(curr.val)
            dfs(curr.right)

        dfs(root)
        self.in_order = in_order
        self.pointer = -1

    def next(self):
        self.pointer += 1
        return self.in_order[self.pointer]

    def hasNext(self):
        return self.pointer + 1 < len(self.in_order)


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        self.stack = [(root, False)]

    def next(self):
        while self.stack:
            curr, visited = self.stack.pop()
            if visited:
                return curr.val
            if curr.right:
                self.stack.append((curr.right, False))
            self.stack.append((curr, True))
            if curr.left:
                self.stack.append((curr.left, False))

    def hasNext(self):
        return len(self.stack) > 0


class Test(unittest.TestCase):
    def test1(self):
        root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
        iterator = BSTIterator(root)
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 7)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 9)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 15)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 20)
        self.assertEqual(iterator.hasNext(), False)


if __name__ == "__main__":
    unittest.main()
