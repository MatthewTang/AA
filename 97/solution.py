import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(2^(n+m), space: O(n+m)
    # memoization: time, space: O(n*m)
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, p = len(s1), len(s2), len(s3)
        if p != n + m:
            return False
        cache = [[-1] * m for _ in range(n)]

        def dfs(i, j) -> bool:
            if i == n and j == m:
                return True
            if i < n and j < m and cache[i][j] != -1:
                return cache[i][j]

            left = right = False
            if i < n and s1[i] == s3[i + j]:
                left = dfs(i + 1, j)
            if j < m and s2[j] == s3[i + j]:
                right = dfs(i, j + 1)
            if i < n and j < m:
                cache[i][j] = left or right
            return left or right

        return dfs(0, 0)

    # dp(bu), time/space: O(n*m)
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, p = len(s1), len(s2), len(s3)
        if p != n + m:
            return False
        n += 1
        m += 1
        dp = [[False] * m for _ in range(n)]
        dp[-1][-1] = True
        # init row
        for c in range(m - 2, -1, -1):
            if s3[c + n - 1] == s2[c]:
                dp[-1][c] = True
            else:
                break
        # init col
        for r in range(n - 2, -1, -1):
            if s3[r + m - 1] == s1[r]:
                dp[r][-1] = True
            else:
                break

        for r in range(n - 2, -1, -1):
            for c in range(m - 2, -1, -1):
                left = True if s1[r] == s3[r + c] and dp[r + 1][c] else False
                right = True if s2[c] == s3[r + c] and dp[r][c + 1] else False
                dp[r][c] = left or right

        return dp[0][0]

    # dp(bu), time: O(n*m), space: O(min(n,m))
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, p = len(s1), len(s2), len(s3)
        if p != n + m:
            return False
        if m > n:
            m, n = n, m
            s2, s1 = s1, s2

        n += 1
        m += 1
        dp = [False] * m
        dp[-1] = True

        # init row
        for c in range(m - 2, -1, -1):
            if s3[c + n - 1] == s2[c]:
                dp[c] = True
            else:
                break

        for r in range(n - 2, -1, -1):
            _dp = [False] * m
            if dp[-1] and s3[r + m - 1] == s1[r]:
                _dp[-1] = True
            for c in range(m - 2, -1, -1):
                left = True if s1[r] == s3[r + c] and dp[c] else False
                right = True if s2[c] == s3[r + c] and _dp[c + 1] else False
                _dp[c] = left or right
            dp = _dp

        return dp[0]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        result = s.is_interleave(s1, s2, s3)
        expected = True
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        result = s.is_interleave(s1, s2, s3)
        expected = False
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        s1 = ""
        s2 = ""
        s3 = ""
        result = s.is_interleave(s1, s2, s3)
        expected = True
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        s1 = "bbbcc"
        s2 = "bbaccbbbabcacc"
        s3 = "bbbbacbcccbcbabbacc"
        result = s.is_interleave(s1, s2, s3)
        expected = False
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
