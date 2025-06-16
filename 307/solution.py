import unittest
from typing import List, Optional


class Node:
    def __init__(self, nums: List[int], left: int, right: int) -> None:
        self.left = left
        self.right = right
        self.middle = (self.left + self.right) // 2
        if self.left == self.right:
            self.sum = nums[self.left]
            return
        self.left_node = Node(nums, self.left, self.middle)
        self.right_node = Node(nums, self.middle + 1, self.right)
        self.sum = self.left_node.sum + self.right_node.sum

    def update(self, index: int, val: int) -> None:
        if index == self.left == self.right:
            self.sum = val
            return
        if index > self.middle:
            self.right_node.update(index, val)
        else:
            self.left_node.update(index, val)
        self.sum = self.left_node.sum + self.right_node.sum

    def sumRange(self, left: int, right: int) -> int:
        if left == self.left and right == self.right:
            return self.sum
        if left > self.middle:
            return self.right_node.sumRange(left, right)
        elif right <= self.middle:
            return self.left_node.sumRange(left, right)
        else:
            return self.left_node.sumRange(
                left, self.middle
            ) + self.right_node.sumRange(self.middle + 1, right)


class NumArray:
    def __init__(self, nums: List[int]) -> None:
        self.root = Node(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.root.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.root.sumRange(left, right)


class Test(unittest.TestCase):
    def test1(self):
        na = NumArray([1, 3, 5])
        self.assertEqual(na.sumRange(0, 2), 9)
        self.assertEqual(na.update(1, 2), None)
        self.assertEqual(na.sumRange(0, 2), 8)


if __name__ == "__main__":
    unittest.main()
