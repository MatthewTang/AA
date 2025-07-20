import unittest
from typing import List, Optional


class Solution:
    def max_profit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)

        def dfs(i: int, rem_cap: int) -> int:
            if i == n:
                return 0

            max_profit = dfs(i + 1, rem_cap)
            if rem_cap >= weight[i]:
                max_profit = max(max_profit, dfs(i, rem_cap - weight[i]) + profit[i])
            return max_profit

        return dfs(0, capacity)

    def max_profit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity + 1
        cache = [[-1] * m for _ in range(n)]

        def dfs(i: int, rem_cap: int) -> int:
            if i == n:
                return 0
            if cache[i][rem_cap] != -1:
                return cache[i][rem_cap]

            max_profit = dfs(i + 1, rem_cap)
            if rem_cap >= weight[i]:
                max_profit = max(max_profit, dfs(i, rem_cap - weight[i]) + profit[i])
            cache[i][rem_cap] = max_profit
            return max_profit

        return dfs(0, capacity)

    def max_profit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity + 1
        dp = [0] * m

        for r in range(n):
            _dp = [0] * m
            for c in range(m):
                _max = dp[c]
                if c >= weight[r]:
                    _max = max(_max, profit[r] + _dp[c - weight[r]])
                _dp[c] = _max
            dp = _dp
        return dp[-1]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        profit = [4, 4, 7, 1]
        weight = [5, 2, 3, 1]
        capacity = 8
        expected = 18
        result = s.max_profit(profit, weight, capacity)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
