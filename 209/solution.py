import unittest
from typing import List, Optional


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = total = 0
        res = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != float("inf") else 0


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [2, 3, 1, 2, 4, 3]
        target = 7
        expected = 2
        result = s.minSubArrayLen(target, nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        target = 4
        nums = [1, 4, 4]
        expected = 1
        result = s.minSubArrayLen(target, nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = 0
        result = s.minSubArrayLen(target, nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
