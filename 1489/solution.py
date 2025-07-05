import unittest
from typing import List, Optional
import heapq


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = {}
        self.rank = {}
        self.components = n

        for i in range(n):
            self.parents[i] = i
            self.rank[i] = 0

    def find(self, node: int) -> int:
        curr = node
        while curr != self.parents[curr]:
            curr = self.parents[curr]

        self.parents[node] = curr

        return curr

    def union(self, node1: int, node2: int) -> bool:
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        rank1, rank2 = self.rank[parent1], self.rank[parent2]

        if rank1 > rank2:
            self.parents[parent2] = parent1
        elif rank1 < rank2:
            self.parents[parent1] = parent2
        else:
            self.parents[parent2] = parent1
            self.rank[parent1] += 1

        self.components -= 1
        return True


class Solution:
    # time: O(E^2(logV)), space: O(E+V)
    def find_critical_and_pseudo_critical_edges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        def mst(n, edges):
            min_heap = []
            uf = UnionFind(n)
            for u, v, w in edges:
                heapq.heappush(min_heap, [w, u, v])
            total = 0
            count = 0
            while count < n - 1 and min_heap:
                w, u, v = heapq.heappop(min_heap)
                if not uf.union(u, v):
                    continue
                total += w
                count += 1
            return total if count == n - 1 else -1

        def mst_include(n, edges, i):
            min_heap = []
            _edge = edges[i]
            edges = edges[:i] + edges[i + 1 :]
            uf = UnionFind(n)
            for u, v, w in edges:
                heapq.heappush(min_heap, [w, u, v])
            total = _edge[2]
            count = 1
            uf.union(_edge[0], _edge[1])
            while count < n - 1 and min_heap:
                w, u, v = heapq.heappop(min_heap)
                if not uf.union(u, v):
                    continue
                total += w
                count += 1
            return total if count == n - 1 else -1

        total = mst(n, edges)
        res = [[], []]

        for i in range(len(edges)):
            _total = mst(n, edges[:i] + edges[i + 1 :])
            if _total == -1 or _total > total:
                res[0].append(i)
                continue
            _total = mst_include(n, edges, i)
            if _total == total:
                res[1].append(i)

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 4
        edges = [[0, 3, 2], [0, 2, 5], [1, 2, 4]]
        result = s.find_critical_and_pseudo_critical_edges(n, edges)
        expected = [[0, 1, 2], []]
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        n = 5
        edges = [
            [0, 3, 2],
            [0, 4, 2],
            [1, 3, 2],
            [3, 4, 2],
            [2, 3, 1],
            [1, 2, 3],
            [0, 1, 1],
        ]
        result = s.find_critical_and_pseudo_critical_edges(n, edges)
        expected = [[4, 6], [0, 1, 2, 3]]
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        n = 5
        edges = [
            [0, 1, 1],
            [1, 2, 1],
            [2, 3, 2],
            [0, 3, 2],
            [0, 4, 3],
            [3, 4, 3],
            [1, 4, 6],
        ]
        result = s.find_critical_and_pseudo_critical_edges(n, edges)
        expected = [[0, 1], [2, 3, 4, 5]]
        self.assertListEqual(result, expected)

    def test4(self):
        s = Solution()
        n = 4
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
        result = s.find_critical_and_pseudo_critical_edges(n, edges)
        expected = [[], [0, 1, 2, 3]]
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
