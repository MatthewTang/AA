import unittest
from typing import List, Optional


class Solution:
    def fname(self, arg):
        return arg


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        arg = 1
        expected = 1
        result = s.fname(arg)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
