import unittest
from typing import List, Optional


class Solution:

    # bf, time: O(n^2), spacd: O(1)
    def trap(self, height: List[int]) -> int:
        def left_max(i: int) -> int:
            max_ = 0
            for j in range(0, i):
                max_ = max(max_, height[j])
            return max_

        def right_max(i: int) -> int:
            max_ = 0
            for j in range(i + 1, len(height)):
                max_ = max(max_, height[j])
            return max_

        out = 0
        for i in range(1, len(height) - 1):
            ml, mr, h = left_max(i), right_max(i), height[i]
            w = max(min(ml, mr) - h, 0)
            # print(i, ml, mr, h, w)
            out += w

        return out

    def trap(self, height: List[int]) -> int:
        prefix_maxs = [0] * len(height)
        p_max = 0
        for i in range(len(height)):
            prefix_maxs[i] = p_max
            p_max = max(p_max, height[i])
        suffix_maxs = [0] * len(height)
        s_max = 0
        for i in range(len(height) - 1, -1, -1):
            suffix_maxs[i] = s_max
            s_max = max(s_max, height[i])
        out = 0
        for i in range(1, len(height) - 1):
            out += max(min(prefix_maxs[i], suffix_maxs[i]) - height[i], 0)

        return out


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        result = s.trap(height)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        height = [4, 2, 0, 3, 2, 5]
        expected = 9
        result = s.trap(height)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
