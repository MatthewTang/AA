import unittest
from typing import List, Optional


class Solution:
    # bf
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        for l in range(len(arr) - k + 1):
            sum_ = 0
            for r in range(l, l + k):
                sum_ += arr[r]
            avg = sum_ / k
            if avg >= threshold:
                count += 1
        return count

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_ = 0
        count = 0
        l = 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                sum_ -= arr[l]
                l += 1
            sum_ += arr[r]
            if r - l + 1 == k:
                avg = sum_ / k
                if avg >= threshold:
                    count += 1
        return count

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_ = sum(arr[: k - 1])
        res = 0
        for l in range(len(arr) - k + 1):
            sum_ += arr[l + k - 1]
            if sum_ / k >= threshold:
                res += 1
            sum_ -= arr[l]
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        arr = [2, 2, 2, 2, 5, 5, 5, 8]
        k = 3
        threshold = 4
        expected = 3
        result = s.numOfSubarrays(arr, k, threshold)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        arr = [12, 2, 2, 2, 5, 5, 5, 8]
        k = 3
        threshold = 4
        expected = 4
        result = s.numOfSubarrays(arr, k, threshold)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
        k = 3
        threshold = 5
        expected = 6
        result = s.numOfSubarrays(arr, k, threshold)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
