import unittest
from typing import List, Optional
from collections import deque


class Solution:
    # dfs
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

        adj = {i: [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
        topSort = []
        visited = set()
        path = set()
        try:
            for i in range(n):
                dfs(i, adj, visited, topSort, path)
        except ValueError:
            return []

        topSort.reverse()
        return topSort

    # bfs
    def topologicalSort(self, edges: List[List[int]], n: int) -> List[int]:
        adj = [set() for _ in range(n)]
        indegree = [0] * n
        for src, dst in edges:
            adj[src].add(dst)
            indegree[dst] += 1

        res = []
        q = deque([i for i in range(n) if indegree[i] == 0])
        while q:
            src = q.popleft()
            res.append(src)
            for dst in adj[src]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    q.append(dst)

        return [] if any(indegree) else res

    def topologicalSort(self, edges: List[List[int]], n: int) -> List[int]:
        seen = set()
        path = set()
        out_edges = [set() for _ in range(n)]
        top_sort = []

        # reverse src, dst
        for src, dst in edges:
            out_edges[dst].add(src)

        def dfs(n):
            if n in path:
                raise ValueError
            if n in seen:
                return
            seen.add(n)
            path.add(n)
            for nei in out_edges[n]:
                dfs(nei)
            top_sort.append(n)
            path.remove(n)

        try:
            for i in range(n):
                dfs(i)
        except:
            return []

        return top_sort


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [6, 7]]
        n = 9
        expected = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [8, 6, 7, 0, 2, 4, 1, 3, 5],
            [0, 6, 8, 1, 2, 7, 3, 4, 5],
        ]
        result = s.topologicalSort(edges, n)
        self.assertTrue(result in expected)

    def test2(self):
        s = Solution()
        edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [6, 7], [3, 0]]
        n = 9
        expected = []
        result = s.topologicalSort(edges, n)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
