from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        '''1 Pass Algo'''
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy

        # create gap of n between slow and fast
        count = 0
        while count <= n:
            fast = fast.next
            count += 1

        # slide the window to fast is at None
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # slow will be step behind node to be removed
        # then to do the removal
        temp = slow.next  # do not need this but not good practice
        slow.next = slow.next.next
        temp.next = None  # do not need this but not good practice

        # return head of list
        return dummy.next
