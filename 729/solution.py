import unittest
from bisect import bisect_left
from typing import List, Optional


# class Node:
#     def __init__(self, nums: List[int], L: int, R: int):
#         self.L = L
#         self.R = R
#         self.M = (self.L + self.R) // 2
#         if self.L == self.R:
#             self.sum = nums[L]
#             self.left = self.right = None
#             return
#         self.left = Node(nums, self.L, self.M)
#         self.right = Node(nums, self.M + 1, self.R)
#         self.sum = self.left.sum + self.right.sum
#
#     def query(self, L: int, R: int) -> int:
#         if self.L == L and self.R == R:
#             return self.sum
#         if R <= self.M:
#             return self.left.query(L, R)
#         elif L > self.M:
#             return self.right.query(L, R)
#         else:
#             return self.left.query(L, self.M) + self.right.query(self.M + 1, R)
#
#     def update(self, index: int, val: int):
#         if index == self.L == self.R:
#             self.sum = val
#             return
#         if index <= self.M:
#             self.left.update(index, val)
#         else:
#             self.right.update(index, val)
#         self.sum = self.left.sum + self.right.sum
#
#
# class SegmentTree:
#     def __init__(self, nums: List[int]):
#         self.root = Node(nums, 0, len(nums) - 1)
#
#     def query(self, L: int, R: int) -> int:
#         return self.root.query(L, R)
#
#     def update(self, index: int, val: int):
#         self.root.update(index, val)
#
#
# class MyCalendar:
#     def __init__(self):
#         self.tree = SegmentTree([0] * (10 ** 9 + 1))
#
#     def book(self, start: int, end: int) -> bool:
#         sum = self.tree.query(start, end - 1)
#         if sum > 0:
#             return False
#         for i in range(start, end):
#             self.tree.update(i, 1)
#         return True


# # bf, time: O(n)
# class MyCalendar:
#     def __init__(self):
#         self.intervals = []
#
#     def book(self, start: int, end: int) -> bool:
#         for i_s, i_e in self.intervals:
#             if not (end <= i_s or start >= i_e):
#                 return False
#
#         self.intervals.append([start, end])
#         return True

# # sorted array, time: O(n)
# class MyCalendar:
#     def __init__(self):
#         self.intervals = []
#
#     def book(self, start: int, end: int) -> bool:
#         i = bisect_left(self.intervals, [start, end])
#
#         if i > 0:
#             _, prev_end = self.intervals[i - 1]
#             if start < prev_end:
#                 return False
#         if i < len(self.intervals):
#             next_start, _ = self.intervals[i]
#             if end > next_start:
#                 return False
#
#         self.intervals.insert(i, [start, end])
#         return True


class Node:
    def __init__(
        self,
        start: int,
        end: int,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
    ):
        self.start = start
        self.end = end
        self.left = left
        self.right = right


# bst, time: O(log n) (avg), O(n) worst case
# iterative
class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True

        curr, prev, right = self.root, None, None
        while curr:
            if start >= curr.end:
                curr, prev, right = curr.right, curr, True
            elif end <= curr.start:
                curr, prev, right = curr.left, curr, False
            else:
                return False
        if right:
            prev.right = Node(start, end)
        else:
            prev.left = Node(start, end)
        return True


# bst, time: O(log n) (avg), O(n) worst case
# recursive
class MyCalendar:
    def __init__(self):
        self.root = None

    def _insert(self, curr: Node, start: int, end: int) -> bool:
        if start >= curr.end:
            if curr.right is None:
                curr.right = Node(start, end)
                return True
            return self._insert(curr.right, start, end)
        elif end <= curr.start:
            if curr.left is None:
                curr.left = Node(start, end)
                return True
            return self._insert(curr.left, start, end)
        else:
            return False

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True

        return self._insert(self.root, start, end)


class Test(unittest.TestCase):
    def test1(self):
        calendar = MyCalendar()
        self.assertTrue(calendar.book(*[10, 20]))
        self.assertFalse(calendar.book(*[15, 25]))
        self.assertTrue(calendar.book(*[20, 30]))

    def test2(self):
        calendar = MyCalendar()
        inputs = [
            [47, 50],
            [33, 41],
            [39, 45],
            [33, 42],
            [25, 32],
            [26, 35],
            [19, 25],
            [3, 8],
            [8, 13],
            [18, 27],
        ]
        expected_outputs = [
            True,
            True,
            False,
            False,
            True,
            False,
            True,
            True,
            True,
            False,
        ]
        for i in range(len(inputs)):
            if expected_outputs[i]:
                self.assertTrue(calendar.book(*inputs[i]))
            else:
                self.assertFalse(calendar.book(*inputs[i]))

    def test3(self):
        calendar = MyCalendar()
        inputs = [
            [97, 100],
            [33, 51],
            [89, 100],
            [83, 100],
            [75, 92],
            [76, 95],
            [19, 30],
            [53, 63],
            [8, 23],
            [18, 37],
            [87, 100],
            [83, 100],
            [54, 67],
            [35, 48],
            [58, 75],
            [70, 89],
            [13, 32],
            [44, 63],
            [51, 62],
            [2, 15],
        ]
        expected_outputs = [
            True,
            True,
            False,
            False,
            True,
            False,
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True,
        ]
        try:

            for i in range(len(inputs)):
                if expected_outputs[i]:
                    self.assertTrue(calendar.book(*inputs[i]))
                else:
                    self.assertFalse(calendar.book(*inputs[i]))
        except:
            print(i)


if __name__ == "__main__":
    unittest.main()
