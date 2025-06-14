import unittest
from typing import List, Optional


class UnionFind:
    def __init__(self, n: int) -> None:
        self.pars = {}
        self.ranks = {}
        self.no_of_components = n
        for i in range(n):
            self.pars[i] = i
            self.ranks[i] = 0

    def find(self, n: int) -> int:
        curr = n
        while curr != self.pars[curr]:
            curr = self.pars[curr]
        self.pars[n] = curr
        return curr

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        ru, rv = self.ranks[pu], self.ranks[pv]

        if ru > rv:
            self.pars[pv] = pu
        elif ru < rv:
            self.pars[pu] = pv
        else:
            self.pars[pv] = pu
            self.ranks[pu] += 1

        self.no_of_components -= 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.no_of_components


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 3
        edges = [[0, 1], [0, 2]]
        expected = 1
        result = s.countComponents(n, edges)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        n = 6
        edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
        expected = 2
        result = s.countComponents(n, edges)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
