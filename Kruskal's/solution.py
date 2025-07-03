import heapq
import unittest
from typing import List, Optional


class UnionFind:
    def __init__(self, n: int) -> None:
        self.pars = []
        self.ranks = []
        for i in range(n):
            self.pars.append(i)
            self.ranks.append(0)

    def find(self, i: int) -> int:
        curr = i
        while curr != self.pars[curr]:
            curr = self.pars[curr]
        self.pars[i] = curr
        return curr

    def union(self, i: int, j: int) -> bool:
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return False
        ri, rj = self.ranks[pi], self.ranks[pj]

        if ri > rj:
            self.pars[pj] = pi
        elif ri < rj:
            self.pars[pi] = pj

        else:
            self.pars[pj] = pi
            self.ranks[pi] += 1

        return True


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        uf = UnionFind(n)
        min_heap = []
        mst = []
        total = 0
        for u, v, w in edges:
            heapq.heappush(min_heap, (w, u, v))

        while len(mst) < n - 1 and min_heap:
            w, u, v = heapq.heappop(min_heap)
            if not uf.union(u, v):
                continue

            mst.append([u, v])
            total += w

        return total if len(mst) == n - 1 else -1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        expected = 11
        edges = [
            [0, 1, 10],
            [0, 2, 3],
            [1, 3, 2],
            [2, 1, 4],
            [2, 3, 8],
            [2, 4, 2],
            [3, 4, 5],
        ]
        result = s.minimumSpanningTree(5, edges)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        expected = -1
        edges = [[0, 1, 4], [1, 2, 7]]
        result = s.minimumSpanningTree(4, edges)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
