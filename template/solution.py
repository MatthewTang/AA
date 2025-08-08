import unittest
from typing import List, Optional


class Solution:
    def fname(self, arg):
        return arg


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        arg = 1
        result = s.fname(arg)
        expected = 1
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
