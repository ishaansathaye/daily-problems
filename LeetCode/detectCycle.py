from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hasCycle = False
        # do not check at the head
        slow = head
        fast = head

        # base cond
        # even list and odd list cases
        # for odd check if .next is None b/c going fast.next.next
        # for even check if fast is None itself since fast at last node
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break

        if not hasCycle:
            return None

        # yes there is cycle
        fast = head  # reset fast pointer
        # move slow "c" distance
        # move fast "a" distance
        # meet at head of cycle
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
