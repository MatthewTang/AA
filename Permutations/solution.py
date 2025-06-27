import unittest
from typing import List, Optional


class Solution:
    def permutations(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums: List[int], path: List[int] = []) -> None:
            if len(nums) == 0:
                res.append(path[:])  # O(n)
                return
            for num in nums:
                path.append(num)
                _nums = nums[:]  # O(n)
                _nums.remove(num)  # O(n)
                dfs(_nums, path)
                path.pop()

        dfs(nums)
        return res

    def permutations(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int = 0) -> List[List[int]]:
            if i == len(nums):
                return [[]]
            paths = dfs(i + 1)
            _paths = []
            num = nums[i]
            for path in paths:
                for j in range(len(path) + 1):
                    _path = path[:]
                    _path.insert(j, num)
                    _paths.append(_path)
            return _paths

        return dfs()

    def permutations(self, nums: List[int]) -> List[List[int]]:
        paths = [[]]
        for i in range(len(nums)):
            num = nums[i]
            _paths = []
            for path in paths:
                for j in range(len(path) + 1):
                    _path = path[:]
                    _path.insert(j, num)
                    _paths.append(_path)
            paths = _paths
        return paths


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [2, 3, 4]
        res = s.permutations(nums)
        expected = [[2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2]]
        self.assertCountEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
