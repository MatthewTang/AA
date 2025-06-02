import unittest
from typing import Deque, List, Optional
from collections import defaultdict, deque


class Solution:
    @staticmethod
    def topSort(
        queue: Deque[int], out_edges: List[List[int]], in_degrees: List[int], n: int
    ) -> List[int]:
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for nxt in out_edges[curr]:
                in_degrees[nxt] -= 1
                if in_degrees[nxt] == 0:
                    queue.append(nxt)

        return order if len(order) == n else []

    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        for grp in range(n):
            items = group[grp]
            if items == -1:
                group[grp] = m
                m += 1

        item_out_edges = [list() for _ in range(n)]
        item_in_degrees = [0] * n

        grp_out_edges = [list() for _ in range(m)]
        grp_in_degrees = [0] * m

        for grp in range(n):
            for b in beforeItems[grp]:
                if group[grp] == group[b]:
                    item_out_edges[b].append(grp)
                    item_in_degrees[grp] += 1
                else:
                    grp_out_edges[group[b]].append(group[grp])
                    grp_in_degrees[group[grp]] += 1

        items_in_grps = [list() for _ in range(m)]
        for grp in range(n):
            items_in_grps[group[grp]].append(grp)

        ordered_items_in_grps = []
        for items in items_in_grps:
            if not items:
                ordered_items_in_grps.append([])
                continue
            ordered_items = self.topSort(
                deque([i for i in items if item_in_degrees[i] == 0]),
                item_out_edges,
                item_in_degrees,
                len(items),
            )
            if not ordered_items:
                return []
            ordered_items_in_grps.append(ordered_items)

        grps = [i for i in range(m)]
        ordered_grps = self.topSort(
            deque([i for i in grps if grp_in_degrees[i] == 0]),
            grp_out_edges,
            grp_in_degrees,
            len(grps),
        )
        if not ordered_grps:
            return []

        return [
            items
            for grp in [ordered_items_in_grps[grp] for grp in ordered_grps]
            for items in grp
        ]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 8
        m = 2
        group = [-1, -1, 1, 0, 0, 1, 0, -1]
        beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
        expected = [6, 3, 4, 5, 2, 0, 7, 1]
        result = s.sortItems(n, m, group, beforeItems)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        n = 8
        m = 2
        group = [-1, -1, 1, 0, 0, 1, 0, -1]
        beforeItems = [[], [6], [5], [6], [3], [], [4], []]
        expected = []
        result = s.sortItems(n, m, group, beforeItems)
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        n = 5
        m = 5
        group = [2, 0, -1, 3, 0]
        beforeItems = [[2, 1, 3], [2, 4], [], [], []]
        expected = [3, 2, 4, 1, 0]
        result = s.sortItems(n, m, group, beforeItems)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
