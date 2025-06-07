from collections import defaultdict
import unittest
from typing import List, Optional


class Solution:
    # time: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = [0] * len(nums)
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            prefix_sums[i] = _sum

        seen = defaultdict(int)
        seen[0] += 1
        res = 0
        for ps in prefix_sums:
            diff = ps - k
            if diff in seen:
                res += seen[diff]
            seen[ps] += 1

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 1, 1]
        k = 2
        expected = 2
        result = s.subarraySum(nums, k)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1, 2, 3]
        k = 3
        expected = 2
        result = s.subarraySum(nums, k)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [3, 2, 1]
        k = 3
        expected = 2
        result = s.subarraySum(nums, k)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        nums = [1, -1, 0]
        k = 0
        expected = 3
        result = s.subarraySum(nums, k)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
