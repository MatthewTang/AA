import unittest
from typing import List, Optional


class Solution:
    def topologicalSort(self, edges: List[List[int]], n: int) -> List[int]:
        def dfs(i, adj, visited, topSort, path):
            if i in path:
                raise ValueError("cyclic detected")
            if i in visited:
                return
            visited.add(i)
            path.add(i)
            for nei in adj[i]:
                dfs(nei, adj, visited, topSort, path)
            topSort.append(i)
            path.remove(i)

        adj = {i: [] for i in range(1, n + 1)}
        for src, dst in edges:
            adj[src].append(dst)
        topSort = []
        visited = set()
        path = set()
        try:
            for i in range(1, n + 1):
                dfs(i, adj, visited, topSort, path)
        except ValueError:
            return []

        topSort.reverse()
        return topSort


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [7, 8]]
        n = 9
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 7, 8, 1, 3, 5, 2, 4, 6]]
        result = s.topologicalSort(edges, n)
        self.assertTrue(result in expected)

    def test2(self):
        s = Solution()
        edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [7, 8], [4, 1]]
        n = 9
        expected = []
        result = s.topologicalSort(edges, n)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
