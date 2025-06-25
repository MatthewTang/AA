import unittest
from typing import List, Optional

from Tree.solution import TreeNode


class Solution:
    # recursive
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(curr: Optional[TreeNode]) -> None:
            if not curr:
                return

            dfs(curr.left)
            dfs(curr.right)
            res.append(curr.val)

        dfs(root)
        return res

    # iterative
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [(root, False)], []

        while stack:
            curr, visited = stack.pop()

            if not curr:
                continue
            if visited:
                res.append(curr.val)
            else:
                stack.append((curr, True))
                stack.append((curr.right, False))
                stack.append((curr.left, False))

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        arg = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        expected = [3, 2, 1]
        result = s.postorderTraversal(arg)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        tree = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
            TreeNode(3, None, TreeNode(8, TreeNode(9))),
        )
        expected = [4, 6, 7, 5, 2, 9, 8, 3, 1]
        result = s.postorderTraversal(tree)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
