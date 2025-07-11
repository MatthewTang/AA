import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(2^n), space: O(n), TLE
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dfs(i: int = 0, s: int = 0) -> int:
            if i == n:
                return 1 if s == target else 0
            return dfs(i + 1, s - nums[i]) + dfs(i + 1, s + nums[i])

        return dfs()

    # cache, time: O(n*m), space: O(n*m), given m = sum(nums)*2+1
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        _sum = sum(nums)
        n, m = len(nums), _sum * 2 + 1
        cache = [[-1] * m for _ in range(n)]

        def dfs(i: int = 0, s: int = 0) -> int:
            if i == n:
                return 1 if s == target else 0
            i_s = s + _sum  # convert s to index of s
            if cache[i][i_s] > -1:
                return cache[i][i_s]
            count = dfs(i + 1, s - nums[i]) + dfs(i + 1, s + nums[i])
            cache[i][i_s] = count
            return count

        return dfs()

    # dp(bu), time: O(n*m), space: O(n*m), given m = sum(nums)*2+1
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        _sum = sum(nums)
        n, m = len(nums), _sum * 2 + 1
        dp = [[0] * m for _ in range(n)]
        for c in range(m):
            plus = 1 if 0 + nums[0] == c - _sum else 0
            minus = 1 if 0 - nums[0] == c - _sum else 0
            dp[0][c] = plus + minus

        for r in range(1, n):
            for c in range(m):
                minus_idx = c - nums[r]
                plus_idx = c + nums[r]
                minus = dp[r - 1][minus_idx] if m > minus_idx >= 0 else 0
                plus = dp[r - 1][plus_idx] if m > plus_idx >= 0 else 0
                dp[r][c] = minus + plus

        return dp[-1][target + _sum] if m > target + _sum >= 0 else 0

    # dp(bu) optimal, time: O(n*m), space: O(m), given m = sum(nums)*2+1
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        _sum = sum(nums)
        n, m = len(nums), _sum * 2 + 1
        dp = [0] * m
        for c in range(m):
            plus = 1 if 0 + nums[0] == c - _sum else 0
            minus = 1 if 0 - nums[0] == c - _sum else 0
            dp[c] = plus + minus

        for r in range(1, n):
            _dp = [0] * m
            for c in range(m):
                minus_idx = c - nums[r]
                plus_idx = c + nums[r]
                minus = dp[minus_idx] if m > minus_idx >= 0 else 0
                plus = dp[plus_idx] if m > plus_idx >= 0 else 0
                _dp[c] = minus + plus
            dp = _dp

        return dp[target + _sum] if m > target + _sum >= 0 else 0


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 1, 1, 1, 1]
        target = 3
        result = s.findTargetSumWays(nums, target)
        expected = 5
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1]
        target = 1
        result = s.findTargetSumWays(nums, target)
        expected = 1
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [
            19,
            24,
            2,
            28,
            27,
            49,
            6,
            45,
            20,
            45,
            34,
            19,
            5,
            0,
            39,
            24,
            48,
            1,
            44,
            23,
        ]
        target = 10
        result = s.findTargetSumWays(nums, target)
        expected = 6056
        self.assertEqual(result, expected)

    def test4(self):
        s = Solution()
        nums = [1]
        target = 2
        result = s.findTargetSumWays(nums, target)
        expected = 0
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        nums = [0]
        target = 0
        result = s.findTargetSumWays(nums, target)
        expected = 2
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
