import unittest
from typing import List, Optional


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = [0] * len(nums)
        postfix_sums = [0] * len(nums)

        _sum = 0
        for i in range(len(nums)):
            prefix_sums[i] = _sum
            _sum += nums[i]

        _sum = 0
        for i in range(len(nums) - 1, -1, -1):
            postfix_sums[i] = _sum
            _sum += nums[i]

        for i in range(len(nums)):
            if prefix_sums[i] == postfix_sums[i]:
                return i

        return -1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 7, 3, 6, 5, 6]
        expected = 3
        result = s.pivotIndex(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1, 2, 3]
        expected = -1
        result = s.pivotIndex(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [2, 1, -1]
        expected = 0
        result = s.pivotIndex(nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
