import unittest
from typing import List, Optional


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum_ = numbers[l] + numbers[r]
            if sum_ == target:
                return [l + 1, r + 1]

            if sum_ > target:
                r -= 1
            else:
                l += 1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        result = s.twoSum(numbers, target)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
