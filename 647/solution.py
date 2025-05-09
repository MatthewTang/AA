import unittest
from typing import List, Optional


class Solution:
    # O(n^2)
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count

    # def countSubstrings(self, s):
    #     def helper(l, r, count):
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             count += 1
    #             l -= 1
    #             r += 1
    #         return count
    #
    #     count = 0
    #     for i in range(len(s)):
    #         count = helper(i, i, count)
    #         count = helper(i, i + 1, count)
    #
    #     return count

    # def helper(self, s, l, r, count):
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         count += 1
    #         l -= 1
    #         r += 1
    #     return count
    #
    # def countSubstrings(self, s):
    #     count = 0
    #     for i in range(len(s)):
    #         count = self.helper(s, i, i, count)
    #         count = self.helper(s, i, i + 1, count)
    #
    #     return count


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "abc"
        expected = 3
        result = sol.countSubstrings(s)
        self.assertIs(result, expected)

    def test2(self):
        sol = Solution()
        s = "aaa"
        expected = 6
        result = sol.countSubstrings(s)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
