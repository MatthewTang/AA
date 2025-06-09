import unittest
from typing import List, Optional


# # bf: time: O(N*n*m), N no. of f calls, n no. of words, m avg len of word, space: O(1)
# class WordFilter:
#     def __init__(self, words: List[str]) -> None:
#         self.words = words
#
#     def f(self, pref: str, suff: str) -> int:
#         res = -1
#         for i, word in enumerate(self.words):
#             if word[: len(pref)] == pref and word[len(word) - len(suff) :] == suff:
#                 res = max(res, i)
#         return res


class WordFilter:
    def __init__(self, words: List[str]) -> None:
        self.mp = {}
        for i, word in enumerate(words):
            for j in range(1, len(word) + 1):
                pref = word[:j]
                for k in range(len(word)):
                    suff = word[k:]
                    self.mp[pref + "}" + suff] = i

    def f(self, pref: str, suff: str) -> int:
        word = pref + "}" + suff
        return self.mp[word] if word in self.mp else -1


class Test(unittest.TestCase):
    def test1(self):
        w = WordFilter(["apple"])
        expected = 0
        result = w.f("a", "e")
        self.assertIs(result, expected)

    def test2(self):
        w = WordFilter(["apple", "a"])
        expected = 1
        result = w.f("a", "a")
        self.assertIs(result, expected)

    def test3(self):
        w = WordFilter(["apple", "are"])
        expected = 1
        result = w.f("a", "e")
        self.assertIs(result, expected)

    def test4(self):
        w = WordFilter(["apple", "are"])
        expected = 0
        result = w.f("ap", "e")
        self.assertIs(result, expected)

    def test5(self):
        w = WordFilter(["apple", "are"])
        expected = -1
        result = w.f("ap", "b")
        self.assertIs(result, expected)

    def test5(self):
        w = WordFilter(["apple", "are"])
        expected = -1
        result = w.f("b", "e")
        self.assertIs(result, expected)

    def test6(self):
        w = WordFilter(["apple", "are", "apple"])
        expected = 2
        result = w.f("a", "e")
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
