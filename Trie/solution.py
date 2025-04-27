import unittest
from typing import List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

    def __repr__(self) -> str:
        return f"TrieNode({self.children}, {self.word})"


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # time: O(m), m = len(word)
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    # time: O(m), m = len(word)
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    # time: O(m), m = len(word)
    def startsWith(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


class Test(unittest.TestCase):
    def test1(self):
        t = Trie()
        t.insert("apple")
        self.assertTrue(t.search("apple"))
        self.assertFalse(t.search("app"))
        self.assertTrue(t.startsWith("app"))
        self.assertFalse(t.startsWith("no"))
        t.insert("nope")
        self.assertTrue(t.startsWith("no"))
        self.assertTrue(t.search("nope"))


if __name__ == "__main__":
    unittest.main()
