import unittest
from typing import List, Optional


# nums:        [1,2,3,5]
# prefix_sums: [1,3,6,11]
class PrefixSum:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.prefix_sums = [0] * len(nums)
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            self.prefix_sums[i] = sum_

    def rangeSum(self, left: int, right: int) -> int:
        prefix_right = self.prefix_sums[right]
        prefix_left = self.prefix_sums[left - 1] if left > 0 else 0
        return prefix_right - prefix_left


class Test(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 5]
        prefix_sum = PrefixSum(nums)
        expected = 8
        result = prefix_sum.rangeSum(2, 3)
        self.assertIs(result, expected)

    def test2(self):
        nums = [1, 2, 3, 5]
        prefix_sum = PrefixSum(nums)
        expected = 8
        result = prefix_sum.rangeSum(2, 3)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
