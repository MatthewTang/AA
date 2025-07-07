import unittest
from typing import List, Optional
from collections import defaultdict
import heapq


class Solution:
    # heap prim's, time: O((n^2)log(n)), space: O(n^2)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)  #
        # n^2
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                adj[i].append((cost, j))
                adj[j].append((cost, i))

        visited = set()
        min_heap = []
        for cost, nei in adj[0]:
            heapq.heappush(min_heap, (cost, 0, nei))
        visited.add(0)
        total_cost = 0

        while min_heap:
            cost, _, dst = heapq.heappop(min_heap)
            if dst in visited:
                continue
            visited.add(dst)
            total_cost += cost
            for cost, nei in adj[dst]:
                if not nei in visited:
                    heapq.heappush(min_heap, (cost, dst, nei))

        return total_cost

    # dense-scan prim's
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        in_mst = [False] * n
        min_edge = [float("inf")] * n
        min_edge[0] = 0

        total = 0
        for _ in range(n):
            u = min((c, i) for i, c in enumerate(min_edge) if not in_mst[i])[1]
            in_mst[u] = True
            total += min_edge[u]
            for v in range(n):
                if not in_mst[v]:
                    p1, p2 = points[u], points[v]
                    cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                    if cost < min_edge[v]:
                        min_edge[v] = cost

        return total


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        result = s.minCostConnectPoints(points)
        expected = 20
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        points = [[3, 12], [-2, 5], [-4, 1]]
        expected = 18
        result = s.minCostConnectPoints(points)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
