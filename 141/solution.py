import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        node0 = ListNode(3)
        node1 = ListNode(2)
        node2 = ListNode(0)
        node3 = ListNode(4)
        node0.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node1
        expected = True
        result = s.hasCycle(node0)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        node0 = ListNode(1)
        node1 = ListNode(2)
        node0.next = node1
        node1.next = node0
        expected = True
        result = s.hasCycle(node0)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        node0 = ListNode(1)
        expected = False
        result = s.hasCycle(node0)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
