import unittest
from typing import List, Optional


class Solution:
    def longest(self, s: str) -> int:
        longest = 0
        res = (0, 0)

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > longest:
                    longest = length
                    res = (l, r)
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > longest:
                    longest = length
                    res = (l, r)
                l -= 1
                r += 1

        print(s[res[0] : res[1] + 1])
        return longest


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "abaab"
        expected = 4
        result = sol.longest(s)
        self.assertIs(result, expected)

    def test2(self):
        solution = Solution()
        s = "cbbd"
        expected = 2
        result = solution.longest(s)
        self.assertIs(result, expected)

    def test3(self):
        solution = Solution()
        s = "babca"
        expected = 3
        result = solution.longest(s)
        self.assertIs(result, expected)

    def test4(self):
        solution = Solution()
        s = "bad"
        expected = 1
        result = solution.longest(s)
        self.assertIs(result, expected)

    def test8(self):
        solution = Solution()
        s = "abbcccbbbcaaccbababcbcabca"
        expected = 7
        result = solution.longest(s)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
