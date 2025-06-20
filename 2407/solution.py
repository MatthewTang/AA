import unittest
from typing import List, Optional


class Solution:
    # recursion, time: O(n(2^n)), space: O(n), TLE
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        res = 0

        def dfs(i):  # O(2^n)
            longest = 0
            for j in range(i + 1, len(nums)):
                if 0 < nums[j] - nums[i] <= k:
                    longest = max(longest, dfs(j))
            return longest + 1

        for i in range(len(nums)):  # O(n)
            res = max(res, dfs(i))
        return res

    # dp(bu), time: O(n^2), space: O(n)
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0
        dp = [1] * len(nums)

        for i in range(n):
            for j in range(i):
                if nums[i] < nums[j]:
                    continue
                if nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return max(dp)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [4, 2, 1, 4, 3, 4, 5, 8, 15]
        k = 3
        expected = 5
        result = s.lengthOfLIS(nums, k)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [7, 4, 5, 1, 8, 12, 4, 7]
        k = 5
        expected = 4
        result = s.lengthOfLIS(nums, k)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [1, 5]
        k = 1
        expected = 1
        result = s.lengthOfLIS(nums, k)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        nums = [i for i in range(1, 100000 + 1)]
        k = 1
        expected = 1
        result = s.lengthOfLIS(nums, k)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
