import unittest
from typing import List, Optional


class Node:
    def __init__(self, nums: List[int], L: int, R: int) -> None:
        self.L = L
        self.R = R
        self.M = (L + R) // 2
        if L == R:
            self.sum = nums[L]
            return
        self.left = Node(nums, self.L, self.M)
        self.right = Node(nums, self.M + 1, self.R)
        self.sum = self.left.sum + self.right.sum

    def update(self, index: int, val: int) -> None:
        if self.L == self.R:
            self.sum = val
            return
        if index <= self.M:
            self.left.update(index, val)
        else:
            self.right.update(index, val)
        self.sum = self.left.sum + self.right.sum

    def query(self, L: int, R: int) -> int:
        if self.L == L and self.R == R:
            return self.sum
        if L > self.M:
            return self.right.query(L, R)
        elif R <= self.M:
            return self.left.query(L, R)
        else:
            return self.left.query(L, self.M) + self.right.query(self.M + 1, R)

    def kth_one(self, k):  # 1-indexed kth 1
        if self.L == self.R:
            return self.L
        if self.left.sum >= k:
            return self.left.kth_one(k)
        return self.right.kth_one(k - self.left.sum)


class SegmentTree:
    def __init__(self, nums) -> None:
        self.root = Node(nums, 0, len(nums) - 1)

    def query(self, L: int, R: int) -> int:
        return self.root.update(L, R)

    def update(self, index: int, val: int) -> None:
        return self.root.update(index, val)

    def kth_empty(self, k):  # 1-indexed
        return self.root.kth_one(k)


class Solution:
    # sort by height des, k asc, time: O(n^2), space: O(n)
    # this runs faster in leetcode since n<= 2000
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))  # O(nlogn)
        res = []
        for p in people:  # O(n)
            res.insert(p[1], p)  # O(n)
        return res

    # binary search and segment tree, time: O(nlogn), space: O(n)
    # asymptotically faster, but tree keeps 4 n ints of auxiliary space
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))  # O(nlogn)
        n = len(people)
        tree = SegmentTree([1] * n)  # O(n)
        res = [[] for _ in range(n)]
        for h, k in people:  # O(n)
            pos = tree.kth_empty(k + 1)  # O(logn)
            res[pos] = [h, k]  # O(1)
            tree.update(pos, 0)  # O(logn)

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        result = s.reconstructQueue(people)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
        expected = [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]
        result = s.reconstructQueue(people)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
