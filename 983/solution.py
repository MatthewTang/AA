import unittest
from typing import List, Optional
from collections import deque


class Solution:
    # bf, time: O(3^n), space: O(n), given n = len(days)
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

    # cache, time: O(n), space: O(n)
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

    # dp(bu), time: O(3n) -> O(n), space: O(n)
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

    # dp(bu), time: O(n), space: O(1)
    def min_cost_tickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp7, dp30 = deque(), deque()
        dp = last7 = last30 = 0

        for i in range(n - 1, -1, -1):
            dp += costs[0]
            while dp7 and dp7[0][0] >= days[i] + 7:
                last7 = dp7.popleft()[1]
            dp = min(dp, last7 + costs[1])
            while dp30 and dp30[0][0] >= days[i] + 30:
                last30 = dp30.popleft()[1]
            dp = min(dp, last30 + costs[2])

            dp7.append([days[i], dp])
            dp30.append([days[i], dp])

        return dp


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
