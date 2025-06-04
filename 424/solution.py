from collections import defaultdict
import unittest
from typing import List, Optional


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map_ = defaultdict(int)
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            map_[s[r]] += 1
            maxf = max(maxf, map_[s[r]])
            while r - l + 1 - maxf > k:
                map_[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

    # def characterReplacement(self, s: str, k: int) -> int:
    #     map_ = defaultdict(int)
    #     l = 0
    #     res = 0
    #     for r in range(len(s)):
    #         map_[s[r]] += 1
    #         while r - l + 1 - map_[s[l]] > k:
    #             map_[s[l]] -= 1
    #             l += 1
    #         res = max(res, r - l + 1)
    #     return res


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "AABABBA"
        k = 1
        expected = 4
        result = sol.characterReplacement(s, k)
        self.assertIs(result, expected)

    def test2(self):
        sol = Solution()
        s = "ABABA"
        k = 0
        expected = 1
        result = sol.characterReplacement(s, k)
        self.assertIs(result, expected)

    def test3(self):
        sol = Solution()
        s = "ABABAA"
        k = 0
        expected = 2
        result = sol.characterReplacement(s, k)
        self.assertIs(result, expected)

    def test4(self):
        sol = Solution()
        s = "ABAB"
        k = 2
        expected = 4
        result = sol.characterReplacement(s, k)
        self.assertIs(result, expected)

    def test5(self):
        sol = Solution()
        s = "ABBB"
        k = 2
        expected = 4
        result = sol.characterReplacement(s, k)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
