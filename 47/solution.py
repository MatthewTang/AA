import unittest
from typing import List, Optional


class Solution:
    # time: O(n * n!), space: O(n)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def dfs(nums: List[int]) -> None:
            if len(nums) == 0:
                res.append(path[:])
                return
            for i, num in enumerate(nums):
                if i + 1 < len(nums) and num == nums[i + 1]:
                    continue
                path.append(num)
                _nums = nums[:i] + nums[i + 1 :]
                dfs(_nums)
                path.pop()

        nums.sort()  # O(nlogn)
        dfs(nums)
        return res

    # time: O(n * n!), space: O(n)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        for i in range(n):
            num = nums[i]
            _res = set()
            for p in res:
                for j in range(len(p) + 1):
                    _p = p.copy()
                    _p.insert(j, num)
                    _res.add(tuple(_p))
            res = [list(t) for t in _res]
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 1, 2]
        result = s.permuteUnique(nums)
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertCountEqual(result, expected)

    def test2(self):
        s = Solution()
        nums = [1, 2, 3]
        result = s.permuteUnique(nums)
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertCountEqual(result, expected)

    def test3(self):
        s = Solution()
        nums = [3, 3, 0, 3]
        result = s.permuteUnique(nums)
        expected = [[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]]
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
