import unittest
from typing import List, Optional


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i: int, path: List[int] = []) -> None:
            if len(path) == k:
                res.append(path[:])
                return
            if i > n:
                return

            path.append(i)
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)

        dfs(1)
        return res

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i: int, path: List[int] = []) -> None:
            if len(path) == k:
                res.append(path[:])
                return

            for j in range(i, n + 1):
                path.append(j)
                dfs(j + 1, path)
                path.pop()

        dfs(1)
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 4
        k = 2
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        result = s.combine(n, k)
        self.assertCountEqual(result, expected)

    def test2(self):
        s = Solution()
        n = 1
        k = 1
        expected = [[1]]
        result = s.combine(n, k)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
