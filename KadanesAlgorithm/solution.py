import unittest
from typing import List, Optional


class Solution:
    # bf: O(n^2)
    def largestSumSubArray(self, nums):
        max_sum = -float("inf")

        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                max_sum = max(max_sum, cur_sum)

        return max_sum

    # dp: time: O(2n) = O(n), space: O(n)
    def largestSumSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]

        return max(dp)

    # Kadane's algo, time: O(n), space: O(1)
    def largestSumSubArray(self, nums):
        prev = largest = nums[0]

        for i in range(1, len(nums)):
            cur = max(prev, 0) + nums[i]
            prev, largest = cur, max(largest, cur)

        return largest

    # sliding window, O(n), space: O(1)
    def largestSumSubArrayIndices(self, nums):
        prev = largest = nums[0]
        l = r = max_l = max_r = 0

        for r in range(1, len(nums)):
            if prev > 0:
                cur = prev + nums[r]
            else:
                cur = nums[r]
                l = r
            if cur > largest:
                max_l, max_r = l, r
            prev = cur

        return [max_l, max_r]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [4, -1, 2, -7, 3, 4]
        expected = 7
        result = s.largestSumSubArray(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [10, -1, 2, -7, 3, 4]
        expected = 11
        result = s.largestSumSubArray(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [4, -1, 2, -7, 3, 4]
        expected = [4, 5]
        result = s.largestSumSubArrayIndices(nums)
        self.assertListEqual(result, expected)

    def test4(self):
        s = Solution()
        nums = [10, -1, 2, -7, 3, 3]
        expected = [0, 2]
        result = s.largestSumSubArrayIndices(nums)
        self.assertListEqual(result, expected)

    def test5(self):
        s = Solution()
        nums = [-2, -3]
        expected = -2
        result = s.largestSumSubArray(nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
