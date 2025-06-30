from collections import defaultdict
import heapq
import unittest
from typing import List, Optional


class Solution:
    # time: O(Elog(E)), space: O(E)
    def minimumSpanningTree(self, edges: List[List[int]], n: int) -> List[List[int]]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        mst = []
        visited = set()
        min_heap = []
        for nei, w in adj[1]:
            heapq.heappush(min_heap, (w, 1, nei))

        visited.add(1)
        total = 0

        while min_heap:
            w, src, nei = heapq.heappop(min_heap)

            if nei in visited:
                continue

            mst.append([src, nei])

            visited.add(nei)
            total += w

            for _nei, weight in adj[nei]:
                if not _nei in visited:
                    heapq.heappush(min_heap, (weight, nei, _nei))

        if len(visited) != n:
            return -1, []

        return total, mst


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 5
        edges = [
            [0, 1, 10],
            [0, 2, 3],
            [1, 3, 2],
            [2, 1, 4],
            [2, 3, 8],
            [2, 4, 2],
            [3, 4, 5],
        ]
        expected = 11
        total, _ = s.minimumSpanningTree(edges, n)
        self.assertIs(total, expected)

    def test2(self):
        s = Solution()
        n = 6
        edges = [
            [0, 1, 10],
            [0, 2, 3],
            [1, 3, 2],
            [2, 1, 4],
            [2, 3, 8],
            [2, 4, 2],
            [3, 4, 5],
        ]
        expected = -1
        total, _ = s.minimumSpanningTree(edges, n)
        self.assertIs(total, expected)


if __name__ == "__main__":
    unittest.main()
