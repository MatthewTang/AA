import unittest
from typing import List, Optional


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        remaining = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
                remaining = 1
            elif remaining > 0:
                nums[l] = nums[r]
                l += 1
                remaining -= 1
        return l


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        expected = 5
        result = s.removeDuplicates(nums)
        self.assertIs(result, expected)
        self.assertListEqual(nums, [1, 1, 2, 2, 3, 3])

    def test2(self):
        s = Solution()
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected = 7
        result = s.removeDuplicates(nums)
        self.assertIs(result, expected)
        self.assertListEqual(nums, [0, 0, 1, 1, 2, 3, 3, 3, 3])

    def test3(self):
        s = Solution()
        nums = [1]
        expected = 1
        result = s.removeDuplicates(nums)
        self.assertIs(result, expected)
        self.assertListEqual(nums, [1])

    def test4(self):
        s = Solution()
        nums = [1, 2, 2, 3]
        expected = 4
        result = s.removeDuplicates(nums)
        self.assertIs(result, expected)
        self.assertListEqual(nums, [1, 2, 2, 3])

    def test5(self):
        s = Solution()
        nums = [1, 2, 2, 2, 3]
        expected = 4
        result = s.removeDuplicates(nums)
        self.assertIs(result, expected)
        self.assertListEqual(nums, [1, 2, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
