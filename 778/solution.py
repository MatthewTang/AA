import unittest
from typing import List, Optional
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap = [(grid[0][0], (0, 0))]
        visited = set()
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            if node == (row - 1, col - 1):
                return weight
            visited.add(node)
            r, c = node
            for dr, dc in directions:
                _r, _c = r + dr, c + dc
                if _r < 0 or _c < 0 or _r >= row or _c >= col or (_r, _c) in visited:
                    continue
                heapq.heappush(min_heap, (max(grid[_r][_c], weight), (_r, _c)))

    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        _min = [float("inf")]
        visited = set()

        def dfs(r, c, weight):
            if r == row - 1 and c == col - 1:
                _min[0] = min(_min[0], weight)
                return
            visited.add((r, c))
            for dr, dc in directions:
                _r, _c = r + dr, c + dc
                if _r < 0 or _c < 0 or _r >= row or _c >= col or (_r, _c) in visited:
                    continue
                dfs(_r, _c, max(grid[_r][_c], weight))
            visited.remove((r, c))

        dfs(0, 0, grid[0][0])
        return _min[0]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [[0, 2], [1, 3]]
        expected = 3
        result = s.swimInWater(grid)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        expected = 16
        result = s.swimInWater(grid)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        grid = [[3, 2], [0, 1]]
        expected = 3
        result = s.swimInWater(grid)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        grid = [
            [10, 12, 4, 6],
            [9, 11, 3, 5],
            [1, 7, 13, 8],
            [2, 0, 15, 14],
        ]
        expected = 14
        result = s.swimInWater(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
