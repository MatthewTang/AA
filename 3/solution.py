import unittest
from typing import List, Optional


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            res = max(res, r - l + 1)
        return res


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "abcabcbb"
        expected = 3
        result = sol.lengthOfLongestSubstring(s)
        self.assertIs(result, expected)

    def test2(self):
        sol = Solution()
        s = "bbbbb"
        expected = 1
        result = sol.lengthOfLongestSubstring(s)
        self.assertIs(result, expected)

    def test3(self):
        sol = Solution()
        s = "pwwkew"
        expected = 3
        result = sol.lengthOfLongestSubstring(s)
        self.assertIs(result, expected)

    def test4(self):
        sol = Solution()
        s = ""
        expected = 0
        result = sol.lengthOfLongestSubstring(s)
        self.assertIs(result, expected)

    def test5(self):
        sol = Solution()
        s = "dvdf"
        expected = 3
        result = sol.lengthOfLongestSubstring(s)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
