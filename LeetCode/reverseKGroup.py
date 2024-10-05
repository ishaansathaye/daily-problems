from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode],
                      k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        begin = dummy
        dummy.next = head
        count = 0
        while curr.next is not None:
            curr = curr.next
            count += 1
            if count % k == 0:
                # make returned value the new begin
                begin = self.reverse(begin, curr.next)
                # start curr at that value
                # value before actual reversing group
                curr = begin
        return dummy.next

    def reverse(self, start, end):
        firstNode = start.next
        prev = start
        curr = start.next
        fast = curr.next
        while fast != end:
            curr.next = prev
            prev = curr
            curr = fast
            fast = fast.next
        curr.next = prev
        # dummy connection to curr (starting after reverse)
        start.next = curr
        # first node that was reversed's connection is to
        # next group's start (end)
        firstNode.next = end
        # returning the beginning
        # of next reverse
        return firstNode
