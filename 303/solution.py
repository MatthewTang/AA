import unittest
from typing import List, Optional


class Solution:
    def __init__(self, nums: List[int]) -> None:
        self.prefix_sums = []
        s = 0
        for n in nums:
            s += n
            self.prefix_sums.append(s)

    def sumRange(self, l: int, r: int) -> int:
        prefix_r = self.prefix_sums[r]
        prefix_l = self.prefix_sums[l - 1] if l > 0 else 0
        return prefix_r - prefix_l


class Test(unittest.TestCase):
    def test1(self):
        s = Solution([-2, 0, 3, -5, 2, -1])
        self.assertIs(s.sumRange(0, 2), 1)
        self.assertIs(s.sumRange(2, 5), -1)
        self.assertIs(s.sumRange(0, 5), -3)


if __name__ == "__main__":
    unittest.main()
