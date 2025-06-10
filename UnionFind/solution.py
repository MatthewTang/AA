import unittest
from typing import List, Optional

# aka disjoint sets
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
            self.parents[node2] = parent1
        elif rank1 < rank2:
            self.parents[node1] = parent2
        else:
            self.parents[node2] = parent1
            self.rank[parent1] += 1

        self.components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.components

    def isSameComponents(self, node1: int, node2):
        return self.find(node1) == self.find(node2)


class Test(unittest.TestCase):
    def test1(self):
        uf = UnionFind(10)
        self.assertIs(uf.getNumComponents(), 10)
        self.assertIs(uf.isSameComponents(1, 3), False)
        self.assertIs(uf.union(1, 2), True)
        self.assertIs(uf.union(2, 3), True)
        self.assertIs(uf.getNumComponents(), 8)
        self.assertIs(uf.isSameComponents(1, 3), True)

    def test2(self):
        uf = UnionFind(10)
        self.assertIs(uf.getNumComponents(), 10)
        self.assertIs(uf.isSameComponents(1, 3), False)
        self.assertIs(uf.union(1, 2), True)
        self.assertIs(uf.union(2, 3), True)
        self.assertIs(uf.union(2, 3), False)
        self.assertIs(uf.getNumComponents(), 8)
        self.assertIs(uf.isSameComponents(1, 3), True)

    def test3(self):
        uf = UnionFind(5)
        self.assertIs(uf.getNumComponents(), 5)

    def test4(self):
        uf = UnionFind(4)
        self.assertIs(uf.union(0, 1), True)
        self.assertIs(uf.getNumComponents(), 3)


if __name__ == "__main__":
    unittest.main()
