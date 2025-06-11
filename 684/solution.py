import unittest
from typing import List, Optional


class UnionFind:
    def __init__(self, n: int) -> None:
        self.pars = {}
        self.ranks = {}
        for i in range(1, n + 1):
            self.pars[i] = i
            self.ranks[i] = 0

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for i, j in edges:
            if not uf.union(i, j):
                return [i, j]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        edges = [[1, 2], [1, 3], [2, 3]]
        expected = [2, 3]
        result = s.findRedundantConnection(edges)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        expected = [1, 4]
        result = s.findRedundantConnection(edges)
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        edges = [[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]
        expected = [2, 5]
        result = s.findRedundantConnection(edges)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
