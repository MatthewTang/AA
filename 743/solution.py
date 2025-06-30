import unittest
from typing import List, Optional
from collections import defaultdict
import heapq


class Solution:
    # dijkstra, time: O(ElogV), space: O(V+E)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        min_heap = [(0, k)]
        shortest = {i: -1 for i in range(1, n + 1)}
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if shortest[node] >= 0:
                continue
            shortest[node] = weight
            for nei, nei_weight in adj[node]:
                if shortest[nei] < 0:
                    heapq.heappush(min_heap, (weight + nei_weight, nei))
        return -1 if min(shortest.values()) == -1 else max(shortest.values())

    # dijkstra, optimal
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        min_heap = [(0, k)]
        visited = set()
        _max = -1
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            _max = max(_max, weight)
            for nei, nei_weight in adj[node]:
                if not nei in visited:
                    heapq.heappush(min_heap, (weight + nei_weight, nei))

        return _max if len(visited) == n else -1

    # dfs, time: O(V*E)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        shortest = {i: float("inf") for i in range(1, n + 1)}

        def dfs(n, time):
            if time >= shortest[n]:
                return
            shortest[n] = time

            for nei, weight in adj[n]:
                dfs(nei, time + weight)

        dfs(k, 0)
        _max = max(shortest.values())

        return -1 if _max == float("inf") else _max


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        expected = 2
        result = s.networkDelayTime(times, n, k)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        times = [[1, 2, 1]]
        n = 2
        k = 1
        expected = 1
        result = s.networkDelayTime(times, n, k)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        times = [[1, 2, 1]]
        n = 2
        k = 2
        expected = -1
        result = s.networkDelayTime(times, n, k)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
