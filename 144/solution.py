import unittest
from typing import List, Optional
from Tree.solution import TreeNode


class Solution:
    # recursive
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(curr: Optional[TreeNode]):
            if curr is None:
                return

            res.append(curr.val)
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return res

    # iterative
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [(root, False)], []
        while stack:
            curr, visited = stack.pop()
            if curr is None:
                continue
            if visited:
                res.append(curr.val)
            else:
                stack.append((curr.right, False))
                stack.append((curr.left, False))
                stack.append((curr, True))

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        expected = [1, 2, 3]
        result = s.preorderTraversal(tree)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        tree = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
            TreeNode(3, None, TreeNode(8, TreeNode(9))),
        )
        expected = [1, 2, 4, 5, 6, 7, 3, 8, 9]
        result = s.preorderTraversal(tree)
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        tree = None
        expected = []
        result = s.preorderTraversal(tree)
        self.assertListEqual(result, expected)

    def test4(self):
        s = Solution()
        tree = TreeNode(1)
        expected = [1]
        result = s.preorderTraversal(tree)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
