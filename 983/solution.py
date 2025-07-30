import unittest
from typing import List, Optional


class Solution:
    def min_cost_tickets(self, days: List[int], costs: List[int]) -> int:
        def dfs(i):
            if i == len(days):
                return 0
            one_day = dfs(i + 1) + costs[0]
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            seven_day = dfs(j) + costs[1]
            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            thirty_day = dfs(j) + costs[2]
            return min(one_day, seven_day, thirty_day)

        return dfs(0)

    # cache
    def min_cost_tickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        cache = [0] * n  # 1 <= costs[i]

        def dfs(i):
            if i == len(days):
                return 0
            if cache[i] != 0:
                return cache[i]
            one_day = dfs(i + 1) + costs[0]
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            seven_day = dfs(j) + costs[1]
            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            thirty_day = dfs(j) + costs[2]
            cache[i] = min(one_day, seven_day, thirty_day)
            return cache[i]

        return dfs(0)

    # dp(bu)
    def min_cost_tickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < n and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp[j])

        return dp[0]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]
        result = s.min_cost_tickets(days, costs)
        expected = 11
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
        costs = [2, 7, 15]
        result = s.min_cost_tickets(days, costs)
        expected = 17
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
