import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        slow2 = head
        while slow2 != slow:
            slow2 = slow2.next
            slow = slow.next

        return slow


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
        result = s.detectCycle(node0)
        self.assertIs(result, node1)

    def test2(self):
        s = Solution()
        node0 = ListNode(1)
        node1 = ListNode(2)
        node0.next = node1
        node1.next = node0
        result = s.detectCycle(node0)
        self.assertIs(result, node0)

    def test3(self):
        s = Solution()
        node0 = ListNode(1)
        result = s.detectCycle(node0)
        self.assertIs(result, None)


if __name__ == "__main__":
    unittest.main()
