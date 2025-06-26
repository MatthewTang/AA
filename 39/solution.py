import unittest
from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int = 0, _sum: int = 0, path: List[int] = []) -> None:
            if _sum == target:
                res.append(path[:])
                return
            if _sum > target:
                return

            for j in range(i, len(candidates)):
                path.append(candidates[j])
                _sum += candidates[j]
                dfs(j, _sum, path)
                _sum -= candidates[j]
                path.pop()

        dfs()
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i=0, _sum=0, path=[]) -> None:
            if _sum == target:
                res.append(path[:])
                return
            if _sum > target:
                return
            if i == len(candidates):
                return

            path.append(candidates[i])
            _sum += candidates[i]
            dfs(i, _sum, path)
            path.pop()
            _sum -= candidates[i]
            dfs(i + 1, _sum, path)

        dfs()
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        result = s.combinationSum(candidates, target)
        self.assertCountEqual(result, expected)

    def test2(self):
        s = Solution()
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        result = s.combinationSum(candidates, target)
        self.assertCountEqual(result, expected)

    def test3(self):
        s = Solution()
        candidates = [2]
        target = 1
        expected = []
        result = s.combinationSum(candidates, target)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
