from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''3 Pointers'''
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        fast = curr.next  # or head.next
        while fast is not None:
            curr.next = prev
            prev = curr
            curr = fast
            fast = fast.next
        curr.next = prev
        return curr

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''3 Pointers with Temp Var'''
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Recursion with Pointers and Temp'''
        if head is None or head.next is None:
            return head
        return self.helper(head, None)

    def helper(self, curr, prev):
        if curr is None:
            return prev
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        return self.helper(curr, prev)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Recursion with No Pointers'''
        # base case
        if head is None or head.next is None:
            # not going to null
            return head

        # setting last element
        reversedHead = self.reverseList(head.next)
        # set the pointer after next to point to current head
        head.next.next = head
        # remove any pointer from head to next in original
        head.next = None
        # send the last element through rec stack
        return reversedHead
