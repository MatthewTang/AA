import unittest
from typing import List, Optional


class Solution:
    # Given a string of characters, return true if it's a palindrome,
    # return false otherwise: O(n)
    def isPalindrome(self, word: str) -> bool:
        l, r = 0, len(word) - 1

        while l < r:
            if word[l] != word[r]:
                return False

            l += 1
            r -= 1

        return True

    # Given a sorted array of integers, return the indices
    # of two elements (in different positions) that sum up to
    # the target value. Assume there is exactly one solution.
    # O(n)
    def targetSum(self, arr: List[int], target: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while l < r:
            sum_ = arr[l] + arr[r]
            if sum_ == target:
                return [l, r]
            elif sum_ > target:
                r -= 1
            else:
                l += 1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        arg = "racecar"
        expected = True
        result = s.isPalindrome(arg)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        arg = "word"
        expected = False
        result = s.isPalindrome(arg)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        arg = "word"
        expected = False
        result = s.isPalindrome(arg)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        arr = [1, 1]
        target = 2
        expected = [0, 1]
        result = s.targetSum(arr, target)
        self.assertListEqual(result, expected)

    def test5(self):
        s = Solution()
        arr = [-1, 1, 2, 4, 5, 6]
        target = 9
        expected = [3, 4]
        result = s.targetSum(arr, target)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
