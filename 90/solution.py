import unittest
from typing import List, Optional


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i: int, path: List[int] = []) -> None:
            if i == len(nums):
                res.append(path[:])
                return

            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, path)

        nums.sort()
        dfs(0)
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(i: int, path: List[int] = []) -> None:
            if i == len(nums):
                res.add(tuple(path))
                return

            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)

        nums.sort()
        dfs(0)
        return [list(t) for t in res]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        arg = [1, 2, 2]
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        result = s.subsetsWithDup(arg)
        self.assertCountEqual(result, expected)

    def test2(self):
        s = Solution()
        arg = [0]
        expected = [[], [0]]
        result = s.subsetsWithDup(arg)
        self.assertCountEqual(result, expected)

    def test3(self):
        s = Solution()
        arg = [4, 4, 4, 1, 4]
        expected = [
            [],
            [1],
            [1, 4],
            [1, 4, 4],
            [1, 4, 4, 4],
            [1, 4, 4, 4, 4],
            [4],
            [4, 4],
            [4, 4, 4],
            [4, 4, 4, 4],
        ]
        result = s.subsetsWithDup(arg)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
