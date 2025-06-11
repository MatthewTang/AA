import unittest
from typing import List, Optional


# dfs, doesn't work when pref, suff overlap
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.index = -1
#
#     def __repr__(self) -> str:
#         return f"TrieNode({self.children}, {self.index})"
#
#
# class Trie:
#     def __init__(self) -> None:
#         self.root = TrieNode()
#
#     def insert(self, word: str, index: int):
#         curr = self.root
#         for c in word:
#             if c in curr.children:
#                 curr = curr.children[c]
#             else:
#                 curr.children[c] = TrieNode()
#                 curr = curr.children[c]
#         curr.index = index
#
#
# class WordFilter:
#     def __init__(self, words: List[str]):
#         self.trie = Trie()
#         for i, w in enumerate(words):
#             self.trie.insert(w, i)
#
#     def f(self, prefix: str, suffix: str):
#         curr = self.trie.root
#         for c in prefix:
#             if c in curr.children:
#                 curr = curr.children[c]
#             else:
#                 return -1
#         res = []
#         if curr.index >= 0 and prefix == suffix:
#             res.append(curr.index)
#
#         def dfs(curr, suffix):
#             if not suffix:
#                 if curr.index >= 0:
#                     res.append(curr.index)
#                 return
#             for c in curr.children:
#                 if c == suffix[0]:
#                     dfs(curr.children[c], suffix[1:])
#                 else:
#                     dfs(curr.children[c], suffix)
#
#         dfs(curr, suffix)
#         return max(res) if res else -1


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


# # hash map, time: init: O(n*m^3), f: O(m), space: O(n*m^3), TLE
# class WordFilter:
#     def __init__(self, words: List[str]) -> None:
#         self.mp = {}
#         for i, word in enumerate(words):
#             for j in range(1, len(word) + 1):
#                 pref = word[:j]
#                 for k in range(len(word)):
#                     suff = word[k:]
#                     self.mp[pref + "$" + suff] = i
#
#     def f(self, pref: str, suff: str) -> int:
#         word = pref + "$" + suff
#         return self.mp[word] if word in self.mp else -1


class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 27
        self.index = -1


# # trie, time: init: O(n*m^3), f: O(m), space: O(n*m^3)
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        pass

    def insert(self, word: str, index: int) -> None:
        curr = self.root
        for ch in word:
            char_index = ord(ch) - ord("a")
            if not curr.children[char_index]:
                curr.children[char_index] = TrieNode()
            curr = curr.children[char_index]
        curr.index = index

    def search(self, word) -> int:
        curr = self.root
        for ch in word:
            char_index = ord(ch) - ord("a")
            if not curr.children[char_index]:
                return -1
            curr = curr.children[char_index]
        return curr.index


class WordFilter:
    def __init__(self, words: List[str]) -> None:
        self.trie = Trie()
        for i, word in enumerate(words):
            for j in range(1, len(word) + 1):
                pref = word[:j]
                for k in range(len(word)):
                    suff = word[k:]
                    self.trie.insert(pref + "{" + suff, i)

    def f(self, pref: str, suff: str) -> int:
        word = pref + "{" + suff
        return self.trie.search(word)


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

    def test7(self):
        w = WordFilter(["apple", "applet"])
        expected = 0
        result = w.f("ap", "e")
        self.assertIs(result, expected)

    def test8(self):
        w = WordFilter(["abc"])
        expected = 0
        result = w.f("ab", "bc")
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
