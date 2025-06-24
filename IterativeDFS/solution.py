import unittest
from typing import List, Optional
from collections import deque
from Tree.solution import TreeNode


def recursive_in_order_dfs(root: Optional[TreeNode]):
    res = []

    def dfs(curr: Optional[TreeNode]):
        if not curr:
            return

        dfs(curr.left)
        res.append(curr.val)
        dfs(curr.right)

    dfs(root)
    return res


def recursive_pre_order_dfs(root: Optional[TreeNode]):
    res = []

    def dfs(curr: Optional[TreeNode]):
        if not curr:
            return

        res.append(curr.val)
        dfs(curr.left)
        dfs(curr.right)

    dfs(root)
    return res


def recursive_post_order_dfs(root: Optional[TreeNode]):
    res = []

    def dfs(curr: Optional[TreeNode]):
        if not curr:
            return

        dfs(curr.left)
        dfs(curr.right)
        res.append(curr.val)

    dfs(root)
    return res


def iterative_in_order_dfs(root: Optional[TreeNode]):
    res = []
    stack = [(root, False)]

    while stack:
        curr, visited = stack.pop()
        if not curr:
            continue
        if visited:
            res.append(curr.val)
        else:
            stack.append((curr.right, False))
            stack.append((curr, True))
            stack.append((curr.left, False))

    return res


def iterative_pre_order_dfs(root: Optional[TreeNode]):
    res = []
    stack = [(root, False)]

    while stack:
        curr, visited = stack.pop()
        if not curr:
            continue
        if visited:
            res.append(curr.val)
        else:
            stack.append((curr.right, False))
            stack.append((curr.left, False))
            stack.append((curr, True))

    return res


def iterative_post_order_dfs(root: Optional[TreeNode]):
    res = []
    stack = [(root, False)]

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


def bfs(root: Optional[TreeNode]):
    q = deque([root])
    lvl = 0
    res = []

    while q:
        # print(f"lvl: {lvl}")
        lvl += 1
        for _ in range(len(q)):
            curr = q.popleft()
            res.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return res


class Test(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.root1 = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )

        self.root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))

    def test1(self):
        res = recursive_in_order_dfs(self.root1)
        self.assertListEqual(res, [4, 2, 5, 1, 6, 3, 7])

    def test2(self):
        res = iterative_in_order_dfs(self.root1)
        self.assertListEqual(res, [4, 2, 5, 1, 6, 3, 7])

    def test3(self):
        res = bfs(self.root1)
        self.assertListEqual(res, [1, 2, 3, 4, 5, 6, 7])

    def test4(self):
        res = recursive_pre_order_dfs(self.root1)
        self.assertListEqual(res, [1, 2, 4, 5, 3, 6, 7])

    def test5(self):
        res = iterative_pre_order_dfs(self.root1)
        self.assertListEqual(res, [1, 2, 4, 5, 3, 6, 7])

    def test6(self):
        res = recursive_post_order_dfs(self.root1)
        self.assertListEqual(res, [4, 5, 2, 6, 7, 3, 1])

    def test7(self):
        res = iterative_post_order_dfs(self.root1)
        self.assertListEqual(res, [4, 5, 2, 6, 7, 3, 1])


if __name__ == "__main__":
    unittest.main()
