import unittest
from typing import List, Optional


class Solution:
    # fixed size sliding window, time: O(n), space: O(n)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])

        return False


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 2, 3, 1]
        k = 3
        expected = True
        result = s.containsNearbyDuplicate(nums, k)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1, 0, 1, 1]
        k = 1
        expected = True
        result = s.containsNearbyDuplicate(nums, k)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        expected = False
        result = s.containsNearbyDuplicate(nums, k)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
