import unittest
from typing import List, Optional


class Solution:
    def find_all_sub_sequences(self, nums):
        res = []

        def dfs(nums, ss):
            if len(nums) == 0:
                if len(ss) > 0:
                    res.append(ss[:])
                return
            if not (len(ss) > 0 and ss[-1] >= nums[0]):
                ss.append(nums[0])
                dfs(nums[1:], ss)
                ss.pop()

                # # w/o append/pop
                # dfs(nums[1:], [*ss, nums[0]])

            dfs(nums[1:], ss)

        dfs(nums, [])
        return res

    def find_all_sub_sequences_2(self, nums):
        res = []

        def dfs(i, ss):
            ss.append(nums[i])
            res.append(ss[:])
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dfs(j, ss)
            ss.pop()

            # # w/o append/pop
            # _ss = ss + [nums[i]]
            # res.append(_ss)
            # for j in range(i + 1, len(nums)):
            #     if nums[j] > nums[i]:
            #         dfs(j, _ss)

        for i in range(len(nums)):
            dfs(i, [])

        return res

    def find_all_sub_sequences_3(self, nums, k):
        res = []

        def dfs(i, ss):
            ss.append(nums[i])
            res.append(ss[:])
            for j in range(i + 1, len(nums)):
                if 0 < nums[j] - nums[i] <= k:
                    dfs(j, ss)
            ss.pop()

            # # w/o append/pop
            # _ss = ss + [nums[i]]
            # res.append(_ss)
            # for j in range(i + 1, len(nums)):
            #     if nums[j] > nums[i]:
            #         dfs(j, _ss)

        for i in range(len(nums)):
            dfs(i, [])

        return res

    def permute(self, nums):
        res = []

        def dfs(nums, path):
            if len(nums) == 0:
                res.append(path[:])
                return
            for num in nums:
                # _nums = nums[:]
                # _nums.remove(num)
                # dfs(_nums, [*path, num])

                _nums = nums[:]
                _nums.remove(num)
                path.append(num)
                dfs(_nums, path)
                path.pop()

        dfs(nums, [])
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [4, 2, 1, 4, 3, 4, 5, 8, 15]
        result1 = s.find_all_sub_sequences(nums)
        result2 = s.find_all_sub_sequences_2(nums)
        result1.sort()
        result2.sort()
        self.assertListEqual(result1, result2)

    def test2(self):
        s = Solution()
        nums = [2, 3, 4]
        res = s.permute(nums)
        expected = [[2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2]]
        self.assertListEqual(res, expected)

    def test3(self):
        s = Solution()
        nums = [4, 2, 1, 4, 3, 4, 5, 8, 15]
        k = 3
        result = s.find_all_sub_sequences_3(nums, k)
        result.sort(key=lambda x: len(x))
        self.assertIs(len(result[-1]), 5)


if __name__ == "__main__":
    unittest.main()
