import unittest
from typing import List, Optional


class Solution:
    def longest_subarray_with_equal_elements(self, nums):
        res = 1
        for i in range(len(nums)):
            prev = nums[i]
            count = 1
            for j in range(i + 1, len(nums)):
                if nums[j] == prev:
                    count += 1
                    res = max(res, count)
                else:
                    break

        return res

    def longest_subarray_with_equal_elements(self, nums):
        l = 0
        res = 0
        count = 0
        for r in range(len(nums)):
            while nums[l] != nums[r]:
                count -= 1
                l += 1
            count += 1
            res = max(res, count)
        return res

    def longest_subarray_with_equal_elements(self, nums):
        l = 0
        res = 0
        for r in range(len(nums)):
            while nums[l] != nums[r]:
                l += 1
            res = max(res, r - l + 1)
        return res

    def longest_sub_array_with_same_values(self, nums):
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == nums[l]:
                res = max(res, r - l + 1)
            else:
                l = r
        return res

    def shortest_subarray_with_target_sum(self, nums, target):
        res = float("inf")
        for i in range(len(nums)):
            total = nums[i]
            for j in range(i + 1, len(nums)):
                total += nums[j]
                if total >= target:
                    res = min(res, j - i + 1)
                    break
        return 0 if res == float("inf") else res

    def shortest_subarray_with_target_sum(self, nums, target):
        res = float("inf")
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != float("inf") else 0


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 2, 2, 3, 3, 3]
        expected = 3
        result = s.longest_subarray_with_equal_elements(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1, 2, 2, 3, 3, 3, 3]
        expected = 4
        result = s.longest_subarray_with_equal_elements(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [1, 1, 1, 1, 1, 1]
        expected = 6
        result = s.longest_subarray_with_equal_elements(nums)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        nums = [2, 3, 1, 2, 4, 3]
        target = 6
        expected = 2
        result = s.shortest_subarray_with_target_sum(nums, target)
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        nums = [1, 1, 1, 1, 1, 1]
        target = 6
        expected = 6
        result = s.shortest_subarray_with_target_sum(nums, target)
        self.assertIs(result, expected)

    def test6(self):
        s = Solution()
        nums = [1, 1, 1, 1, 1]
        target = 6
        expected = 0
        result = s.shortest_subarray_with_target_sum(nums, target)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
