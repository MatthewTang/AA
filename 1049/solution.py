import unittest
from typing import List, Optional


class Solution:
    def last_stone(self, stones: int) -> int:
        total = sum(stones)
        capacity = total // 2  # shdnt matter ie 2 > 1/1.5
        n = len(stones)

        def dfs(i: int, rem_cap: int) -> int:
            if i == n:
                return 0
            max_sum = dfs(i + 1, rem_cap)
            if rem_cap >= stones[i]:
                max_sum = max(
                    max_sum,
                    (0 if rem_cap == stones[i] else dfs(i + 1, rem_cap - stones[i]))
                    + stones[i],
                )
            return max_sum

        return total - 2 * dfs(0, capacity)

    def last_stone(self, stones: int) -> int:
        total = sum(stones)
        cap = total // 2
        n, m = len(stones), cap + 1
        cache = [[-1] * m for _ in range(n)]

        def dfs(i: int, rem_cap: int) -> int:
            if i == n:
                return 0
            if cache[i][rem_cap] != -1:
                return cache[i][rem_cap]
            max_sum = dfs(i + 1, rem_cap)
            if rem_cap >= stones[i]:
                max_sum = max(max_sum, dfs(i + 1, rem_cap - stones[i]) + stones[i])
            cache[i][rem_cap] = max_sum
            return max_sum

        return total - 2 * dfs(0, cap)

    def last_stone(self, stones: int) -> int:
        total = sum(stones)
        cap = total // 2
        n, m = len(stones), cap + 1
        dp = [0] * m

        # init
        for c in range(m):
            dp[c] = stones[0] if c >= stones[0] else 0

        for r in range(1, n):
            _dp = [0] * m
            for c in range(m):
                _max = dp[c]
                if c >= stones[r]:
                    _max = max(_max, dp[c - stones[r]] + stones[r])
                _dp[c] = _max
            dp = _dp

        return total - dp[-1] * 2


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        stones = [2, 7, 4, 1, 8, 1]
        expected = 1
        result = s.last_stone(stones)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        stones = [31, 26, 33, 21, 40]
        expected = 5
        result = s.last_stone(stones)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
