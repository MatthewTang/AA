import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(2^(n+m)), space: O(n+m)
    # memoization, time/space: O(n*m)
    def shortest_common_supersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        cache = [[-1] * m for _ in range(n)]

        def dfs(i, j) -> str:
            if i == n and j == m:
                return ""
            if i == n:
                return str2[j:]
            if j == m:
                return str1[i:]
            if cache[i][j] != -1:
                return cache[i][j]
            if str1[i] == str2[j]:
                return str1[i] + dfs(i + 1, j + 1)
            left = str1[i] + dfs(i + 1, j)
            right = str2[j] + dfs(i, j + 1)
            cache[i][j] = left if len(left) < len(right) else right
            return cache[i][j]

        return dfs(0, 0)

    # dp(tu), time/space: O(n*m)
    def shortest_common_supersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1) + 1, len(str2) + 1
        dp = [[""] * m for _ in range(n)]
        for c in range(m - 2, -1, -1):
            dp[-1][c] = str2[c:]
        for r in range(n - 2, -1, -1):
            dp[r][-1] = str1[r:]

        for r in range(n - 2, -1, -1):
            for c in range(m - 2, -1, -1):
                if str1[r] == str2[c]:
                    dp[r][c] = str1[r] + dp[r + 1][c + 1]
                else:
                    left = str1[r] + dp[r + 1][c]
                    right = str2[c] + dp[r][c + 1]
                    dp[r][c] = left if len(left) < len(right) else right
        return dp[0][0]

    # dp(tu), time: O(n*m), space: O(min(n,m))
    def shortest_common_supersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1) + 1, len(str2) + 1
        if m > n:
            n, m = m, n
            str1, str2 = str2, str1

        dp = [""] * m
        for c in range(m - 2, -1, -1):
            dp[c] = str2[c:]

        for r in range(n - 2, -1, -1):
            _dp = [""] * m
            _dp[-1] = str1[r:]
            for c in range(m - 2, -1, -1):
                if str1[r] == str2[c]:
                    _dp[c] = str1[r] + dp[c + 1]
                else:
                    left = str1[r] + dp[c]
                    right = str2[c] + _dp[c + 1]
                    _dp[c] = left if len(left) < len(right) else right
            dp = _dp
        return dp[0]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        str1 = "abac"
        str2 = "cab"
        result = s.shortest_common_supersequence(str1, str2)
        expected = "cabac"
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        str1 = "aaaaaaaa"
        str2 = "aaaaaaaa"
        result = s.shortest_common_supersequence(str1, str2)
        expected = "aaaaaaaa"
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        str1 = "a"
        str2 = "b"
        result = s.shortest_common_supersequence(str1, str2)
        expected = "ba"
        self.assertTrue(result in expected)


if __name__ == "__main__":
    unittest.main()
