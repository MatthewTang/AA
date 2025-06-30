import unittest
from typing import List, Optional
from collections import defaultdict
import heapq


class Solution:
    # dijkstra, time: O(V+E log(V)), space: O(V+E)
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = defaultdict(list)
        for i, (src, dst) in enumerate(edges):
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))

        max_heap = [(-1, start_node)]
        visited = set()
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            if node == end_node:
                return -prob
            if node in visited:
                continue
            visited.add(node)
            for nei, nei_prob in adj[node]:
                if not nei in visited:
                    heapq.heappush(max_heap, (nei_prob * prob, nei))
        return 0


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.2]
        start = 0
        end = 2
        expected = 0.25
        result = s.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.3]
        start = 0
        end = 2
        expected = 0.3
        result = s.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(result, expected)

    def test3(self):
        s = Solution()
        n = 3
        edges = [[0, 1]]
        succProb = [0.5]
        start = 0
        end = 2
        expected = 0
        result = s.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
