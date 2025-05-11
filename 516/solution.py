import unittest
from typing import List, Optional
from functools import lru_cache


class Solution:
    # # O(n*2^n)
    # def longestPalindromeSubseq(self, s):
    #     def isPalidrome(s):
    #         l, r = 0, len(s) - 1
    #
    #         while r > l:
    #             if s[l] != s[r]:
    #                 return False
    #             l += 1
    #             r -= 1
    #
    #         return True
    #
    #     ss = set()
    #
    #     def dfs(i, ss):
    #         if i >= len(s):
    #             return
    #         _ss = set()
    #         for w in ss:
    #             _ss.add(w + s[i])
    #         ss |= _ss
    #         ss.add(s[i])
    #
    #         dfs(i + 1, ss)
    #
    #     # O(n*2^n)
    #     dfs(0, ss)
    #
    #     longest = 0
    #
    #     # O(2^n)
    #     for s in ss:
    #         if isPalidrome(s): #O(n)
    #             longest = max(longest, len(s))
    #
    #     return longest

    # # dp(tp), time: O(n^2), space: O(n^2)
    # def longestPalindromeSubseq(self, s):
    #     cache = [[-1] * len(s) for _ in range(len(s))]
    #
    #     def dfs(l, r):
    #         if l < 0 or r >= len(s):
    #             return 0
    #         if cache[l][r] != -1:
    #             return cache[l][r]
    #
    #         if s[l] == s[r]:
    #             _l = 2
    #             if l == r:
    #                 _l = 1
    #             cache[l][r] = _l + dfs(l - 1, r + 1)
    #         else:
    #             cache[l][r] = max(dfs(l - 1, r), dfs(l, r + 1))
    #
    #         return cache[l][r]
    #
    #     longest = 0
    #     for i in range(len(s)):
    #         longest = max(longest, dfs(i, i))
    #         longest = max(longest, dfs(i, i + 1))
    #
    #     return longest

    # # dp(tp), time: O(n^2), space: O(n^2)
    # def longestPalindromeSubseq(self, s):
    #     cache = {}
    #
    #     def dfs(l, r):
    #         if l < 0 or r >= len(s):
    #             return 0
    #         if (l, r) in cache:
    #             return cache[l, r]
    #
    #         if s[l] == s[r]:
    #             _l = 1 if l == r else 2
    #             cache[l, r] = _l + dfs(l - 1, r + 1)
    #         else:
    #             cache[l, r] = max(dfs(l - 1, r), dfs(l, r + 1))
    #
    #         return cache[l, r]
    #
    #     longest = 0
    #     for i in range(len(s)):
    #         longest = max(longest, dfs(i, i))
    #         longest = max(longest, dfs(i, i + 1))
    #
    #     return longest

    # use lcs, O(n^2)
    def longestPalindromeSubseq(self, s: str) -> int:
        def lcs(s1: str, s2: str) -> int:
            dp = [0] * (len(s2) + 1)

            for i in range(len(s1) - 1, -1, -1):
                prev = 0
                for j in range(len(s2) - 1, -1, -1):
                    if s1[i] == s2[j]:
                        dp[j], prev = 1 + prev, dp[j]
                    else:
                        dp[j], prev = max(dp[j], dp[j + 1]), dp[j]

            return dp[0]

        return lcs(s, s[::-1])


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "bbbab"
        expected = 4
        result = sol.longestPalindromeSubseq(s)
        self.assertIs(result, expected)

    def test2(self):
        sol = Solution()
        s = "cbbd"
        expected = 2
        result = sol.longestPalindromeSubseq(s)
        self.assertIs(result, expected)

    def test3(self):
        sol = Solution()
        s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
        expected = 159
        result = sol.longestPalindromeSubseq(s)
        self.assertIs(result, expected)

    def test4(self):
        sol = Solution()
        s = "a"
        expected = 1
        result = sol.longestPalindromeSubseq(s)
        self.assertIs(result, expected)

    def test5(self):
        sol = Solution()
        s = "aabaa"
        expected = 5
        result = sol.longestPalindromeSubseq(s)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
