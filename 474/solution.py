import unittest
from typing import List, Optional
from collections import Counter


class Solution:
    def largest_subset(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)

        cache: List[List[List[int]]] = [
            [[-1] * (m + 1) for _ in range(n + 1)] for _ in range(l)
        ]

        def _count(s: str) -> List[int]:
            m, n = 0, 0
            for i in range(len(s)):
                if s[i] == "0":
                    m += 1
                else:
                    n += 1
            return m, n

        def dfs(i: int, rem_m: int, rem_n: int) -> int:
            if i == l:
                return 0

            if cache[i][rem_n][rem_m] > -1:
                return cache[i][rem_n][rem_m]

            max_ = dfs(i + 1, rem_m, rem_n)

            c_m, c_n = _count(strs[i])

            if rem_m >= c_m and rem_n >= c_n:
                max_ = max(max_, dfs(i + 1, rem_m - c_m, rem_n - c_n) + 1)

            cache[i][rem_n][rem_m] = max_
            return max_

        return dfs(0, m, n)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        strs = ["10", "0001", "111001", "1", "0"]
        m = 5
        n = 3
        result = s.largest_subset(strs, m, n)
        expected = 4
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        strs = ["10", "0", "1"]
        m = 1
        n = 1
        result = s.largest_subset(strs, m, n)
        expected = 2
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        strs = ["00011", "00001", "00001", "0011", "111"]
        m = 8
        n = 5
        result = s.largest_subset(strs, m, n)
        expected = 3
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        strs = [
            "0",
            "11",
            "1000",
            "01",
            "0",
            "101",
            "1",
            "1",
            "1",
            "0",
            "0",
            "0",
            "0",
            "1",
            "0",
            "0110101",
            "0",
            "11",
            "01",
            "00",
            "01111",
            "0011",
            "1",
            "1000",
            "0",
            "11101",
            "1",
            "0",
            "10",
            "0111",
        ]
        m = 9
        n = 80
        result = s.largest_subset(strs, m, n)
        expected = 17
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
