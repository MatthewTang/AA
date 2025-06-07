import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        curr = head
        while curr:
            curr = curr.next
            c += 1

        m = c // 2
        curr = head
        c = 0
        while c < m:
            curr = curr.next
            c += 1

        return curr

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        expected = ListNode(3, ListNode(4, ListNode(5)))
        head = ListNode(1, ListNode(2, expected))
        result = s.middleNode(head)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        expected = ListNode(4, ListNode(5, ListNode(6)))
        head = ListNode(1, ListNode(2, ListNode(3, expected)))
        result = s.middleNode(head)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
