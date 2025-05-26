import unittest
from typing import Dict, List, Optional, Set


class Solution:
    # topological, time: O(V+E), space: (V+E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            adj[src].append(dst)

        visited = set()
        path = set()

        def dfs(
            i: int,
            adj: Dict[int, List[int]],
            visited: Set[int],
            path: Set[int],
            res: List[int],
        ):
            if i in path:
                raise ValueError
            if i in visited:
                return
            visited.add(i)
            path.add(i)
            for n in adj[i]:
                dfs(n, adj, visited, path, res)
            path.remove(i)
            res.append(i)

        try:
            for i in range(numCourses):
                dfs(i, adj, visited, path, res)
        except ValueError:
            return []

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [0, 1]
        result = s.findOrder(numCourses, prerequisites)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected = [[0, 2, 1, 3], [0, 1, 2, 3], [0, 2, 1, 3]]
        result = s.findOrder(numCourses, prerequisites)
        self.assertTrue(result in expected)

    def test3(self):
        s = Solution()
        numCourses = 1
        prerequisites = []
        expected = [0]
        result = s.findOrder(numCourses, prerequisites)
        self.assertListEqual(result, expected)

    def test4(self):
        s = Solution()
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [0, 3]]
        expected = []
        result = s.findOrder(numCourses, prerequisites)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
