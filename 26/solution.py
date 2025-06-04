import unittest
from typing import List, Optional


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        k = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                nums[k] = nums[r]
                k += 1
                l = r
        return k


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 1, 2]
        expected = 2
        result = s.removeDuplicates(nums)
        self.assertIs(result, expected)
        self.assertListEqual(nums, [1, 2, 2])

    def test2(self):
        s = Solution()
        nums = [1]
        expected = 1
        result = s.removeDuplicates(nums)
        self.assertIs(result, expected)
        self.assertListEqual(nums, [1])

    def test3(self):
        s = Solution()
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = 5
        result = s.removeDuplicates(nums)
        self.assertIs(result, expected)
        self.assertListEqual(nums, [0, 1, 2, 3, 4, 2, 2, 3, 3, 4])


if __name__ == "__main__":
    unittest.main()
