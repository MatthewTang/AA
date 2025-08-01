import unittest
from typing import List, Optional


class Solution:
    # dp(bu), time: O(n*m), space: O(m)
    def lcs(self, s1: List[str], s2: List[str]) -> int:
        n, m = len(s1) + 1, len(s2) + 1
        dp = [0] * m

        for r in range(n - 2, -1, -1):
            _dp = [0] * m
            for c in range(m - 2, -1, -1):
                if s1[r] == s2[c]:
                    _dp[c] = 1 + dp[c + 1]
                else:
                    _dp[c] = max(dp[c], _dp[c + 1])
            dp = _dp

        print(f"space: O({m})")
        return dp[0]

    # dp(bu) optimised, time: O(n*m), space: O(min(m,n))
    def lcs(self, s1: List[str], s2: List[str]) -> int:
        n, m = len(s1) + 1, len(s2) + 1
        if m > n:
            m, n = n, m
            s2, s1 = s1, s2

        dp = [0] * m

        for r in range(n - 2, -1, -1):
            _dp = [0] * m
            for c in range(m - 2, -1, -1):
                if s1[r] == s2[c]:
                    _dp[c] = 1 + dp[c + 1]
                else:
                    _dp[c] = max(dp[c], _dp[c + 1])
            dp = _dp

        print(f"space: O({m})")
        return dp[0]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        s1 = ["A", "D", "C", "B"]
        s2 = ["A", "B", "C"]
        result = s.lcs(s1, s2)
        expected = 2
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        s1 = ["A", "B", "C"]
        s2 = ["A", "D", "C", "B"]
        result = s.lcs(s1, s2)
        expected = 2
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
