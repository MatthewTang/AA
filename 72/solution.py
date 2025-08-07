import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(3^(m+n)), space(m+n)
    def min_operations(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        def dfs(i, j) -> int:
            if i == n and j == m:
                return 0
            if i == n:
                return dfs(i, j + 1) + 1
            if j == m:
                return dfs(i + 1, j) + 1

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            insert = dfs(i, j + 1)
            delete = dfs(i + 1, j)
            replace = dfs(i + 1, j + 1)
            return min(insert, delete, replace) + 1

        return dfs(0, 0)

    # memoization, time: O(n*m), space(m*n)
    def min_operations(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        cache = [[-1] * m for _ in range(n)]

        def dfs(i, j) -> int:
            if i == n and j == m:
                return 0
            if i == n:
                return dfs(i, j + 1) + 1
            if j == m:
                return dfs(i + 1, j) + 1

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            if cache[i][j] != -1:
                return cache[i][j]

            insert = dfs(i, j + 1)
            delete = dfs(i + 1, j)
            replace = dfs(i + 1, j + 1)
            cache[i][j] = min(insert, delete, replace) + 1
            return cache[i][j]

        return dfs(0, 0)

    # dp(bu), time: O(n*m), space(m*n)
    def min_operations(self, word1: str, word2: str) -> int:
        n, m = len(word1) + 1, len(word2) + 1  # extra row/col for init
        dp = [[0] * m for _ in range(n)]

        # init row
        for c, j in zip(range(m - 2, -1, -1), range(1, m)):
            dp[-1][c] = j
        # init col
        for r, i in zip(range(n - 2, -1, -1), range(1, n)):
            dp[r][-1] = i

        for r in range(n - 2, -1, -1):
            for c in range(m - 2, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = min(dp[r][c + 1], dp[r + 1][c], dp[r + 1][c + 1]) + 1

        return dp[0][0]

    # dp(bu), time: O(n*m), space(min(m*n))
    def min_operations(self, word1: str, word2: str) -> int:
        n, m = len(word1) + 1, len(word2) + 1  # extra row/col for init
        if m > n:
            n, m = m, n
            word1, word2 = word2, word1

        dp = [0] * m

        # init row
        for c, j in zip(range(m - 2, -1, -1), range(1, m)):
            dp[c] = j

        for r, i in zip(range(n - 2, -1, -1), range(1, n)):
            _dp = [0] * m
            _dp[-1] = i
            for c in range(m - 2, -1, -1):
                if word1[r] == word2[c]:
                    _dp[c] = dp[c + 1]
                else:
                    _dp[c] = min(_dp[c + 1], dp[c], dp[c + 1]) + 1
            dp = _dp

        return dp[0]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        word1 = "horse"
        word2 = "ros"
        result = s.min_operations(word1, word2)
        expected = 3
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        word1 = "intention"
        word2 = "execution"
        result = s.min_operations(word1, word2)
        expected = 5
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        word1 = "intention"
        word2 = "intention"
        result = s.min_operations(word1, word2)
        expected = 0
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
