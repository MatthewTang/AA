from collections import defaultdict
import unittest
from typing import Dict, List, Optional
import heapq


class Solution:
    def shortest(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        min_heap = [(0, src)]
        shortest = {i: -1 for i in range(n)}

        while min_heap:
            weight, node = heapq.heappop(min_heap)

            if shortest[node] >= 0:
                continue

            shortest[node] = weight

            for nei, nei_weight in adj[node]:
                if shortest[nei] < 0:
                    heapq.heappush(min_heap, (weight + nei_weight, nei))

        return shortest


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
        src = 0
        expected = {0: 0, 1: 7, 2: 3, 3: 9, 4: 5}
        result = s.shortest(n, edges, src)
        self.assertDictEqual(result, expected)

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
        src = 0
        expected = {0: 0, 1: 7, 2: 3, 3: 9, 4: 5, 5: -1}
        result = s.shortest(n, edges, src)
        self.assertDictEqual(result, expected)

    def test3(self):
        s = Solution()
        n = 4
        edges = [[0, 1, 5], [0, 2, 7], [1, 2, 2], [1, 3, 6], [2, 3, 4]]
        src = 1
        expected = {0: -1, 1: 0, 2: 2, 3: 6}
        result = s.shortest(n, edges, src)
        self.assertDictEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
