import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(n^2), space: O(1)
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                w = (j - i) * min(height[i], height[j])
                res = max(res, w)

        return res

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            w = (r - l) * min(height[l], height[r])
            res = max(res, w)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        result = s.maxArea(height)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        height = [1, 1]
        expected = 1
        result = s.maxArea(height)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
