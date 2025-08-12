import unittest
from typing import List, Optional, Tuple
from bisect import bisect_left


def compress(nums: List[int]) -> Tuple[List[int], dict]:
    vals = sorted(set(nums))
    to_idx = {v: i for i, v in enumerate(vals)}
    return vals, to_idx


class SegMax:
    def __init__(self, n: int):
        self.N = 1
        while self.N < n:
            self.N <<= 1
        self.t = [0] * (2 * self.N)

    def update(self, i: int, val: int) -> None:
        i += self.N
        if val > self.t[i]:
            self.t[i] = val
            i //= 2
            while i:
                self.t[i] = max(self.t[2 * i], self.t[2 * i + 1])
                i //= 2

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        l += self.N
        r += self.N
        ans = 0
        while l <= r:
            if l & 1:
                ans = max(ans, self.t[l])
                l += 1
            if not (r & 1):
                ans = max(ans, self.t[r])
                r -= 1
            l //= 2
            r //= 2
        return ans


class Solution:
    # recursion, time: O(n(2^n)), space: O(n), TLE
    # def lengthOfLIS(self, nums: List[int], k: int) -> int:
    #     res = 0

    #     def dfs(i):  # O(2^n)
    #         longest = 0
    #         for j in range(i + 1, len(nums)):
    #             if 0 < nums[j] - nums[i] <= k:
    #                 longest = max(longest, dfs(j))
    #         return longest + 1

    #     for i in range(len(nums)):  # O(n)
    #         res = max(res, dfs(i))
    #     return res

    # dp(bu), time: O(n^2), space: O(n)
    # def lengthOfLIS(self, nums: List[int], k: int) -> int:
    #     n, res = len(nums), 0
    #     dp = [1] * len(nums)

    #     for i in range(n):
    #         for j in range(i):
    #             if nums[i] < nums[j]:
    #                 continue
    #             if nums[i] - nums[j] <= k:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #         res = max(res, dp[i])
    #     return max(dp)

    # # bf, time: O(2^n), space: O(n), TLE
    # def lengthOfLIS(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #
    #     def dfs(i: int, prev: Optional[int]) -> int:
    #         if i == n:
    #             return 0
    #         skip = dfs(i + 1, prev)
    #         include = 0
    #         if prev is None or k >= nums[i] - prev > 0:
    #             include = dfs(i + 1, nums[i]) + 1
    #         return max(skip, include)
    #
    #     return dfs(0, None)
    #
    # # memoization: time/space: O(n*m), MLE
    # def lengthOfLIS(self, nums: List[int], k: int) -> int:
    #     n, m = len(nums), max(nums) + 1
    #     cache = [[-1] * m for _ in range(n)]  # let j = 0 if prev is None
    #
    #     def dfs(i: int, prev: Optional[int]) -> int:
    #         if i == n:
    #             return 0
    #         j = 0 if prev is None else prev
    #         if cache[i][j] != -1:
    #             return cache[i][j]
    #         skip = dfs(i + 1, prev)
    #         include = 0
    #         if prev is None or k >= nums[i] - prev > 0:
    #             include = dfs(i + 1, nums[i]) + 1
    #         cache[i][j] = max(skip, include)
    #         return cache[i][j]
    #
    #     return dfs(0, None)

    # def lengthOfLIS(self, nums: List[int], k: int) -> int:
    #     n, m = len(nums) + 1, max(nums) + 1
    #     dp = [[0] * m for _ in range(n)]
    #     for r in range(n - 2, -1, -1):
    #         for c in range(m - 1, -1, -1):
    #             max_ = dp[r + 1][c]
    #             if c == 0 or k >= nums[r] - c > 0:
    #                 max_ = max(max_, dp[r + 1][nums[r]] + 1)
    #             dp[r][c] = max_
    #     return dp[0][0]
    #
    # def lengthOfLIS(self, nums: List[int], k: int) -> int:
    #     n, m = len(nums) + 1, max(nums) + 1
    #     dp = [0] * m
    #     for r in range(n - 2, -1, -1):
    #         _dp = [0] * m
    #         for c in range(m - 1, -1, -1):
    #             max_ = dp[c]
    #             if c == 0 or k >= nums[r] - c > 0:
    #                 max_ = max(max_, dp[nums[r]] + 1)
    #             _dp[c] = max_
    #         dp = _dp
    #     return dp[0]

    # def lengthOfLIS(self, nums: List[int], k: int) -> int:
    #     if not nums:
    #         return 0
    #     vals, to_idx = compress(nums)
    #     U = len(vals)
    #     dp = [0] * U  # dp[i] = best LIS ending at vals[i]
    #     ans = 0
    #     for v in nums:
    #         L = bisect_left(vals, v - k)
    #         R = bisect_left(vals, v) - 1
    #         if L <= R:
    #             best = max(dp[L : R + 1])
    #         else:
    #             best = 0
    #         cur = best + 1
    #         idx = to_idx[v]
    #         dp[idx] = max(dp[idx], cur)
    #         ans = max(ans, cur)
    #     return ans

    # def lengthOfLIS(self, nums: List[int], k: int) -> int:
    #     """Segment tree version (O(n log U))."""
    #     if not nums:
    #         return 0
    #     vals, to_idx = compress(nums)
    #     seg = SegMax(len(vals))
    #     ans = 0
    #     for v in nums:
    #         L = bisect_left(vals, v - k)
    #         R = bisect_left(vals, v) - 1
    #         best = seg.query(L, R)
    #         cur = best + 1
    #         seg.update(to_idx[v], cur)
    #         if cur > ans:
    #             ans = cur
    #     return ans

    # def lengthOfLIS(self, nums: List[int], k: int) -> int:
    #     vals = sorted(set(nums))
    #     val_to_idx = {val: i for i, val in enumerate(vals)}
    #     dp = [0] * len(vals)
    #     ans = 0
    #     for num in nums:
    #         left = bisect_left(vals, num - k)
    #         # right = bisect_left(vals, num) - 1
    #         right = val_to_idx[num] - 1

    #         best = max(dp[left : right + 1]) if left <= right else 0
    #         curr = best + 1
    #         idx = val_to_idx[num]
    #         dp[idx] = max(dp[idx], curr)
    #         ans = max(ans, dp[idx])
    #     return ans

    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        vals = sorted(set(nums))
        val_to_idx = {v: i for i, v in enumerate(vals)}
        seg = SegMax(len(vals))
        ans = 0
        for v in nums:
            L = bisect_left(vals, v - k)
            R = bisect_left(vals, v) - 1
            best = seg.query(L, R) if L <= R else 0
            curr = best + 1
            idx = val_to_idx[v]
            seg.update(idx, curr)
            ans = max(ans, curr)
        return ans


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [4, 2, 1, 4, 3, 4, 5, 8, 15]
        k = 3
        expected = 5
        result = s.lengthOfLIS(nums, k)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [7, 4, 5, 1, 8, 12, 4, 7]
        k = 5
        expected = 4
        result = s.lengthOfLIS(nums, k)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [1, 5]
        k = 1
        expected = 1
        result = s.lengthOfLIS(nums, k)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        nums = [i for i in range(1, 100000 + 1)]
        k = 1
        expected = 100000
        result = s.lengthOfLIS(nums, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
