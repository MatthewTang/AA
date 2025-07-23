import unittest
from typing import List, Optional


class Solution:
    def fewest_no_of_coin(self, coins: List[int], amount: int) -> int:
        n, m = len(coins), amount + 1
        dp = [float("inf")] * m
        dp[0] = 0

        for r in range(n):
            _dp = [float("inf")] * m
            _dp[0] = 0
            for c in range(1, m):
                _min = dp[c]
                if c >= coins[r]:
                    _min = min(_min, 1 + _dp[c - coins[r]])
                _dp[c] = _min
            dp = _dp

        return -1 if dp[-1] == float("inf") else dp[-1]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        coins = [1, 2, 5]
        amount = 11
        expected = 3
        result = s.fewest_no_of_coin(coins, amount)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        coins = [2]
        amount = 3
        expected = -1
        result = s.fewest_no_of_coin(coins, amount)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        coins = [1]
        amount = 0
        expected = 0
        result = s.fewest_no_of_coin(coins, amount)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
