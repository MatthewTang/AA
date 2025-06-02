import unittest
from typing import List, Optional


class Solution:
    def duplicates(self, nums: List[int], k: int) -> bool:
        for l in range(len(nums)):
            for r in range(l + 1, min(l + k, len(nums))):
                if nums[l] == nums[r]:
                    return True
        return False

    def duplicates(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if r - l + 1 > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 2, 3, 2, 3, 3]
        k = 3
        expected = True
        result = s.duplicates(nums, k)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1, 2, 3, 4, 2, 6]
        k = 3
        expected = False
        result = s.duplicates(nums, k)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
