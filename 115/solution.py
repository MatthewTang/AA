import unittest
from typing import List, Optional
from functools import lru_cache


class Solution:
    # bf, time: O(2^n), space: O(n)
    def count(self, s: str, t: str) -> int:
        n = len(s)

        def dfs(i: int, _s: str) -> int:
            if i == n:
                return 0
            if not t.startswith(_s):
                return 0
            skip = dfs(i + 1, _s)
            s_ = _s + s[i]
            include = 1 if s_ == t else dfs(i + 1, s_)

            return skip + include

        return dfs(0, "")

    def count(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        def dfs(i: int, j: int) -> int:
            if j == m:
                return 1
            if i == n:
                return 0

            skip = dfs(i + 1, j)
            include = 0
            if s[i] == t[j]:
                include = dfs(i + 1, j + 1)

            return skip + include

        return dfs(0, 0)

    # memoization, time: O(n*m), space: O(n*m)
    def count(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        cache = [[-1] * m for _ in range(n)]

        def dfs(i: int, j: int) -> int:
            if j == m:
                return 1
            if i == n:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]

            skip = dfs(i + 1, j)
            include = 0
            if s[i] == t[j]:
                include = dfs(i + 1, j + 1)
            cache[i][j] = skip + include

            return skip + include

        return dfs(0, 0)

    def count(self, s: str, t: str) -> int:
        n, m = len(s) + 1, len(t) + 1
        dp = [[0] * m for _ in range(n)]
        for r in range(n):
            dp[r][-1] = 1

        for r in range(n - 2, -1, -1):
            for c in range(m - 2, -1, -1):
                skip = dp[r + 1][c]
                include = 0 if s[r] != t[c] else dp[r + 1][c + 1]
                dp[r][c] = skip + include

        return dp[0][0]

    def count(self, s: str, t: str) -> int:
        n, m = len(s) + 1, len(t) + 1
        dp = [0] * m
        dp[-1] = 1

        for r in range(n - 2, -1, -1):
            _dp = [0] * m
            _dp[-1] = 1
            for c in range(m - 2, -1, -1):
                skip = dp[c]
                include = 0 if s[r] != t[c] else dp[c + 1]
                _dp[c] = skip + include
            dp = _dp

        return dp[0]


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "rabbbit"
        t = "rabbit"
        result = sol.count(s, t)
        expected = 3
        self.assertIs(result, expected)

    def test2(self):
        sol = Solution()
        s = "abc"
        t = "abc"
        result = sol.count(s, t)
        expected = 1
        self.assertIs(result, expected)

    def test3(self):
        sol = Solution()
        s = "ababc"
        t = "abc"
        result = sol.count(s, t)
        expected = 3
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
