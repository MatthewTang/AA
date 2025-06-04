import unittest
from typing import List, Optional


class Solution:
    def isPalidrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not self.alphaNumeric(s[l]):
                l += 1
                continue
            if not self.alphaNumeric(s[r]):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    @staticmethod
    def alphaNumeric(c):
        return (
            ord("a") <= ord(c) <= ord("z")
            or ord("A") <= ord(c) <= ord("Z")
            or ord("0") <= ord(c) <= ord("9")
        )


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        arg = "racecar"
        expected = True
        result = s.isPalidrome(arg)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        arg = "A man, a plan, a canal: Panama"
        expected = True
        result = s.isPalidrome(arg)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        arg = " "
        expected = True
        result = s.isPalidrome(arg)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
