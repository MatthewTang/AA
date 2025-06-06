import unittest
from typing import List, Optional


class Solution:
    def productExceptSelf(self, nums: List[int]):
        l = len(nums)
        prefix_products = [0] * l
        suffix_products = [0] * l

        p = 1
        for i in range(l):
            prefix_products[i] = p
            p *= nums[i]

        p = 1
        for i in range(l - 1, -1, -1):
            suffix_products[i] = p
            p *= nums[i]

        res = [0] * l
        for i in range(l):
            res[i] = prefix_products[i] * suffix_products[i]

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        result = s.productExceptSelf(nums)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        result = s.productExceptSelf(nums)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
