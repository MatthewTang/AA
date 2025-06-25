import unittest
from typing import List, Optional
from bisect import bisect_left
import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.nums = []

    # O(n)
    def addNum(self, num: int) -> None:
        i = bisect_left(self.nums, num)
        self.nums.insert(i, num)

    # [1,2,3]
    # len = 3
    # k1 = (3-1)//2 = 1
    # k2 = 3//2 = 1
    # median = (2+2)/2 = 1

    # [1,2]
    # len = 2
    # k1 = (2-1)//2 = 0
    # k2 = 2//2 = 1
    # median = (1+2)/2 = 1.5
    def findMedian(self) -> int:
        k1 = (len(self.nums) - 1) // 2
        k2 = len(self.nums) // 2
        return (self.nums[k1] + self.nums[k2]) / 2


# assume numbers in range [0,100]
class MedianFinder:
    def __init__(self) -> None:
        self.counts = [0] * 101
        self.total = 0

    def addNum(self, num: int) -> None:
        if not 0 <= num <= 100:
            raise ValueError("value must be in [0, 100]")

        self.counts[num] += 1
        self.total += 1

    def findMedian(self) -> int:
        k1 = (self.total - 1) // 2
        k2 = self.total // 2

        running = 0
        v1 = v2 = None

        for num, count in enumerate(self.counts):
            running += count

            if v1 is None and running > k1:
                v1 = num
            if running > k2:
                v2 = num
                break

        return (v1 + v2) / 2


class MedianFinder:
    def __init__(self) -> None:
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if (self.small and self.large) and (-self.small[0] > self.large[0]):
            _max = -heapq.heappop(self.small)
            heapq.heappush(self.large, _max)
        if len(self.small) > len(self.large) + 1:
            _max = -heapq.heappop(self.small)
            heapq.heappush(self.large, _max)
        if len(self.large) > len(self.small) + 1:
            _min = heapq.heappop(self.large)
            heapq.heappush(self.small, -_min)

    def findMedian(self) -> int:
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (self.large[0] + -self.small[0]) / 2


class Test(unittest.TestCase):
    def test1(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2)

    def test2(self):
        mf = MedianFinder()
        mf.addNum(1)
        self.assertEqual(mf.findMedian(), 1)
        mf.addNum(2)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2)
        mf.addNum(4)
        self.assertEqual(mf.findMedian(), 2.5)


if __name__ == "__main__":
    unittest.main()
