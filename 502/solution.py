import unittest
from typing import List, Optional
import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        l = [i for i in zip(capital, profits)]
        l.sort(key=lambda x: x[0])
        maxheap = []
        i = 0
        while k > 0:
            while i < len(l) and l[i][0] <= w:
                heapq.heappush(maxheap, -l[i][1])
                i += 1
            if not maxheap:
                break
            w += -heapq.heappop(maxheap)
            k -= 1
        return w

    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        min_heap = [i for i in zip(capital, profits)]  # O(n)
        heapq.heapify(min_heap)  # O(n log n)
        max_heap = []

        while k > 0:  # O(k)
            while min_heap and min_heap[0][0] <= w:
                _, p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -p)
            if not max_heap:
                break
            k -= 1
            w += -heapq.heappop(max_heap)

        return w


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 1]
        expected = 4
        result = s.findMaximizedCapital(k, w, profits, capital)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
