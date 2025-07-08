import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(2^n), space: O(n)
    def max_profit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)

        def dfs(i, c):
            if i == n:
                return 0

            # skip
            p = dfs(i + 1, c)
            # include
            if c - weight[i] >= 0:
                p = max(p, dfs(i + 1, c - weight[i]) + profit[i])
            return p

        return dfs(0, capacity)

    # dp(td), time: O(m*n), space: O(m*n)
    def max_profit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity + 1
        cache = [[-1] * m for _ in range(n)]

        def dfs(i, c):
            if i == n:
                return 0
            # cache
            if cache[i][c] >= 0:
                return cache[i][c]

            # skip
            p = dfs(i + 1, c)
            # include
            if c - weight[i] >= 0:
                p = max(p, dfs(i + 1, c - weight[i]) + profit[i])
            cache[i][c] = p
            return p

        return dfs(0, capacity)

    # dp(bu), time: O(m*n), space: O(m*n)
    def max_profit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity + 1
        dp = [[0] * n for _ in range(m)]

        # init dp
        for r in range(m):
            dp[r][0] = 0
        for c in range(n):
            dp[0][c] = profit[0] if weight[0] <= c else 0

        # build up dp iteratively
        for r in range(1, m):
            for c in range(1, n):
                skip = dp[r - 1][c]
                include = 0
                if c >= weight[r]:
                    include = profit[r] + dp[-1][c - weight[r]]
                dp[r][c] = max(skip, include)

        return dp[-1][-1]

    # dp(bu) optimal, time: O(m*n), space: O(n)
    def max_profit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity + 1
        dp = [0] * m

        # init dp
        for c in range(m):
            dp[c] = profit[0] if weight[0] <= c else 0

        # build up dp iteratively
        for r in range(1, n):
            _dp = [0] * m
            for c in range(1, m):
                skip = dp[c]
                include = 0
                if c >= weight[r]:
                    include = profit[r] + dp[c - weight[r]]
                _dp[c] = max(skip, include)
            dp = _dp

        return dp[-1]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        profit = [4, 4, 7, 1]
        weight = [5, 2, 3, 1]
        capacity = 8
        expected = 12
        result = s.max_profit(profit, weight, capacity)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
