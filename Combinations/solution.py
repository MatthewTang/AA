import unittest
from typing import List, Optional


class Solution:
    # time: O(k * 2^n)
    def combinations(self, n: int, k: int) -> List[int]:
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

    # time: O(k * C(n, k))
    def combinations(self, n: int, k: int) -> List[int]:
        res = []
        def dfs(i: int, path: List[int] = []) -> None:
            if len(path) == k:
                res.append(path[:])
                return
            if i> n:
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
        expected = [
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [2, 3],
            [2, 4],
            [2, 5],
            [3, 4],
            [3, 5],
            [4, 5],
        ]
        result = s.combinations(5, 2)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
