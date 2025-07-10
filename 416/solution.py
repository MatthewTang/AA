import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(2^n), space: O(n), TLE
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)

        def dfs(i=0, _sum=0):
            if i == n:
                return _sum == total - _sum
            # skip
            skip = dfs(i + 1, _sum)
            # include
            include = dfs(i + 1, _sum + nums[i])

            return skip or include

        return dfs()

    # memoization, time: O(n*m), space: O(n*m), given m = sum(nums) +1
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)

        cache = [[None] * (total + 1) for _ in range(n)]

        def dfs(i=0, _sum=0):
            if i == n:
                return _sum == total - _sum

            if cache[i][_sum] != None:
                return cache[i][_sum]

            # skip
            skip = dfs(i + 1, _sum)
            # include
            include = dfs(i + 1, _sum + nums[i])

            cache[i][_sum] = skip or include

            return skip or include

        return dfs()

    # dp(bu), time: O(n*m), space: O(n*m), given m = sum(nums) +1
    def canPartition(self, nums: List[int]) -> bool:
        n, m = len(nums), sum(nums) + 1
        dp = [[False] * m for _ in range(n)]
        # init dp
        for r in range(n):
            dp[r][0] = False
        for c in range(m):
            dp[0][c] = True if c - (2 * nums[0]) == 0 else False
        # iterate and build up dp
        for r in range(1, n):
            for c in range(1, m):
                skip = dp[r - 1][c]
                include = False
                remain = c - (2 * nums[r])
                if remain >= 0:
                    include = dp[r - 1][remain]
                dp[r][c] = skip or include

        return dp[-1][-1]

    # dp(bu) optimal, time: O(n*m), space: O(n)
    def canPartition(self, nums: List[int]) -> bool:
        n, m = len(nums), sum(nums) + 1
        dp = [False] * m

        for c in range(m):
            dp[c] = True if c - nums[0] == nums[0] else False

        for r in range(1, n):
            _dp = [False] * m
            for c in range(1, m):
                skip = dp[c]
                remain_sum = c - (2 * nums[r])
                include = False
                if remain_sum >= 0:
                    include = dp[remain_sum]
                _dp[c] = skip or include
            dp = _dp

        return dp[-1]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 5, 11, 5]
        expected = True
        result = s.canPartition(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1, 2, 3, 5]
        expected = False
        result = s.canPartition(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [1, 2, 5]
        expected = False
        result = s.canPartition(nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
