import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next: Optional[ListNode] = next

    def to_list(self) -> list:
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return result

    def __repr__(self) -> str:
        return str(self.to_list())


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        res = 0
        while prev and slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
        expected = 6
        result = s.pairSum(head)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
        expected = 7
        result = s.pairSum(head)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        head = ListNode(1, ListNode(100000))
        expected = 100001
        result = s.pairSum(head)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
