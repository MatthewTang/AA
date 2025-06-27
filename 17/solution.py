import unittest
from typing import List, Optional


class Solution:
    # recursive backtrack
    # time: O(n*4^n), space: O(n) stack
    def letterCombinations(self, digits: str) -> List[str]:
        _map = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        res = []

        def dfs(i: int = 0, path: str = ""):
            if i == len(digits):
                res.append(path)  # O(1)
                return
            num = int(digits[i])
            for char in _map[num]:
                dfs(i + 1, path + char)  # O(n)

        if digits:
            dfs()  # O(4^n)
        return res

    # iteration
    # time: O(n*4^n), space: O(n)
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        _map = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        res = [""]
        for i in range(len(digits)):
            tmp = []
            for combination in res:
                for char in _map[int(digits[i])]:
                    tmp.append(combination + char)
            res = tmp
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        digits = "23"
        result = s.letterCombinations(digits)
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertCountEqual(result, expected)

    def test2(self):
        s = Solution()
        digits = ""
        result = s.letterCombinations(digits)
        expected = []
        self.assertCountEqual(result, expected)

    def test3(self):
        s = Solution()
        digits = "2"
        result = s.letterCombinations(digits)
        expected = ["a", "b", "c"]
        self.assertCountEqual(result, expected)

    def test4(self):
        s = Solution()
        digits = "7"
        result = s.letterCombinations(digits)
        expected = ["p", "q", "r", "s"]
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
