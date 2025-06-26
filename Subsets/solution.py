import unittest
from typing import List, Optional


class Solution:
    # time: O(n^2)
    def pairs(self, nums):
        res = []
        for i in range(len(nums)):  # O(n)
            for j in range(i + 1, len(nums)):  # O(n)
                res.append([nums[i], nums[j]])  # O(1)
        return res

    # # time: O(n * 2^n)
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     subsets = []
    #
    #     def dfs(nums: List[int], path: List[int] = []):
    #         if len(nums) == 0:
    #             # subsets.append(path[:])
    #             # return
    #
    #             subsets.append(path)
    #             return
    #
    #         # target = nums[0]
    #         # nums = nums[1:]
    #         # path.append(target)
    #         # dfs(nums, path)
    #         # path.pop()
    #         # dfs(nums, path)
    #
    #         dfs(nums[1:], [*path, nums[0]])
    #         dfs(nums[1:], path[:])
    #
    #     dfs(nums)
    #
    #     return subsets

    # time: O(n * 2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(i: int, cur_set: List[int] = []):  # O(2^n)
            if i == len(nums):

                subsets.append(cur_set[:])  # O(n)
                return

            # decision to include nums[i]
            cur_set.append(nums[i])
            dfs(i + 1, cur_set)

            # decision not to include nums[i]
            cur_set.pop()
            dfs(i + 1, cur_set)

        dfs(0)
        return subsets

    # # iterative
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     subsets, stack = [], [(0, [])]
    #
    #     while stack:
    #         i, cur_set = stack.pop()
    #         if i == len(nums):
    #             subsets.append(cur_set)
    #         else:
    #             stack.append((i + 1, cur_set + [nums[i]]))
    #             stack.append((i + 1, cur_set))
    #
    #     return subsets

    # hash set, time: O(n*2^n), space: O(2^n)
    def subsets_with_duplicates(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(i: int, cur_set: List[int] = []):  # O(2^n)
            if i == len(nums):
                res.add(tuple(cur_set))
                return

            # decision to include nums[i]
            cur_set.append(nums[i])
            dfs(i + 1, cur_set)

            # decision not to include nums[i]
            cur_set.pop()
            dfs(i + 1, cur_set)

        nums.sort()
        dfs(0)
        return [list(t) for t in res]

    # back-tracking, time: O(n*2^n), space: O(2^n)
    def subsets_with_duplicates(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i: int, path: List[int] = []):
            if i == len(nums):
                res.append(path[:])
                return

            path.append(nums[i])
            dfs(i + 1, path)

            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, path)

        nums.sort()
        dfs(0)
        return res


def canon(seq_of_seqs):
    """Convert a list of lists → multiset of tuples so order never matters."""
    return [tuple(sorted(s)) for s in seq_of_seqs]


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def _check(self, fn, args, expected):
        self.assertCountEqual(canon(fn(*args)), canon(expected))

    def test1(self):
        self._check(self.s.pairs, [[1, 2, 3]], [[1, 2], [2, 3], [1, 3]])

    def test2(self):
        self._check(
            self.s.subsets,
            [[1, 2, 3]],
            [[], [1], [1, 2], [1, 3], [2], [2, 3], [3], [1, 2, 3]],
        )

    # give list of nums that are not necessarily distinct, return all *distinct* subsets
    def test4(self):
        self._check(
            self.s.subsets_with_duplicates,
            [[1, 2, 3, 2]],
            [
                [],
                [1],
                [1, 2],
                [1, 3],
                [2],
                [2, 3],
                [3],
                [1, 2, 3],
                [1, 2, 3, 2],
                [1, 2, 2],
                [2, 3, 2],
                [2, 2],
            ],
        )

    def test5(self):
        self._check(
            self.s.subsets_with_duplicates,
            [[1, 1, 2]],
            [[1, 1, 2], [1, 1], [1, 2], [1], [2], []],
        )


if __name__ == "__main__":
    unittest.main()
