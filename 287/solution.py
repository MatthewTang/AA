import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(n^2), space: O(1), TLE
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]

    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])

    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n] < 0:
                return n
            nums[n] = -nums[n]

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 3, 4, 2, 2]
        expected = 2
        result = s.findDuplicate(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [3, 1, 3, 4, 2]
        expected = 3
        result = s.findDuplicate(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [3, 3, 3, 3, 3]
        expected = 3
        result = s.findDuplicate(nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
