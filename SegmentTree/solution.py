import unittest
from typing import List, Optional


class Node:
    def __init__(self, nums: List[int], L: int, R: int):
        self.L = L
        self.R = R
        self.M = (L + R) // 2
        if self.L == self.R:
            self.sum = nums[self.L]
            return
        self.left = Node(nums, self.L, self.M)
        self.right = Node(nums, self.M + 1, self.R)
        self.sum = self.left.sum + self.right.sum

    def update(self, i: int, val: int):
        if self.L == self.R == i:
            self.sum = val
            return
        if i > self.M:
            self.right.update(i, val)
        else:
            self.left.update(i, val)
        self.sum = self.right.sum + self.left.sum

    def query(self, l: int, r: int):
        if self.L == l and self.R == r:
            return self.sum
        if l > self.M:
            return self.right.query(l, r)
        elif r <= self.M:
            return self.left.query(l, r)
        else:
            return self.left.query(l, self.M) + self.right.query(self.M + 1, r)


class SegmentTree:
    # O(n)
    def __init__(self, nums: List[int]) -> None:
        self.root = Node(nums, 0, len(nums) - 1)

    # O(logn)
    def update(self, i: int, val: int):
        self.root.update(i, val)

    # O(logn)
    def query(self, l: int, r: int) -> int:
        return self.root.query(l, r)


class Test(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 4, 5]
        s = SegmentTree(nums)
        self.assertEqual(s.query(0, 2), 6)
        self.assertEqual(s.query(2, 4), 12)
        self.assertEqual(s.update(3, 0), None)
        self.assertEqual(s.query(2, 4), 8)

    def test2(self):
        nums = [-1, 2, 4]
        s = SegmentTree(nums)
        self.assertEqual(s.query(0, 1), 1)
        self.assertEqual(s.query(1, 2), 6)
        self.assertEqual(s.update(2, 3), None)
        self.assertEqual(s.query(0, 2), 4)


if __name__ == "__main__":
    unittest.main()
