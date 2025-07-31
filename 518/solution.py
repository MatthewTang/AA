import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(2^m), space: O(m), given m = amount
    def count(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        def dfs(i, rem_amount):
            if rem_amount == 0:
                return 1
            if i == n:
                return 0
            skip = dfs(i + 1, rem_amount)
            include = 0
            if coins[i] <= rem_amount:
                include = dfs(i, rem_amount - coins[i])
            return include + skip

        return dfs(0, amount)

    # memoization, time: O(n*m), space: O(n*m), given n = len(coins), m = amount
    def count(self, amount: int, coins: List[int]) -> int:
        n, m = len(coins), amount + 1
        cache = [[-1] * m for _ in range(n)]

        def dfs(i, rem_amount):
            if rem_amount == 0:
                return 1
            if i == n:
                return 0
            if cache[i][rem_amount] != -1:
                return cache[i][rem_amount]
            skip = dfs(i + 1, rem_amount)
            include = 0
            if coins[i] <= rem_amount:
                include = dfs(i, rem_amount - coins[i])
            cache[i][rem_amount] = include + skip
            return include + skip

        return dfs(0, amount)

    # dp(bu), time: O(n*m), space: O(n*m)
    def count(self, amount: int, coins: List[int]) -> int:
        n, m = len(coins), amount + 1
        dp = [[0] * m for _ in range(n)]
        for c in range(m):
            skip = 1 if c == 0 else 0
            include = dp[0][c - coins[0]] if c >= coins[0] else 0
            dp[0][c] = skip + include

        for r in range(1, n):
            for c in range(m):
                skip = dp[r - 1][c]
                include = dp[r][c - coins[r]] if c >= coins[r] else 0
                dp[r][c] = skip + include
        return dp[-1][-1]

    # dp(bu), time: O(n*m), space: O(n)
    def count(self, amount: int, coins: List[int]) -> int:
        n, m = len(coins), amount + 1
        dp = [0] * m
        for c in range(m):
            skip = 1 if c == 0 else 0
            include = dp[c - coins[0]] if c >= coins[0] else 0
            dp[c] = skip + include

        for r in range(1, n):
            _dp = [0] * m
            for c in range(m):
                skip = dp[c]
                include = _dp[c - coins[r]] if c >= coins[r] else 0
                _dp[c] = skip + include
            dp = _dp
        return dp[-1]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        amount = 5
        coins = [1, 2, 5]
        result = s.count(amount, coins)
        expected = 4
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        amount = 3
        coins = [2]
        result = s.count(amount, coins)
        expected = 0
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        amount = 10
        coins = [10]
        result = s.count(amount, coins)
        expected = 1
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        amount = 0
        coins = [10]
        result = s.count(amount, coins)
        expected = 1
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
