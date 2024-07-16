# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        # find middle
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        fast = self.reverse(slow.next) # setting fast pointer to head of reversed list
        slow.next = None # making end None (removing its pointer)
        slow = head

        # merge the 2 parts of original list
        while fast is not None:
            temp = slow.next
            slow.next = fast
            fast = fast.next # moving fast before losing its pointer to its next
            slow.next.next = temp
            slow = temp

    def reverse(self, node):
        prev = None
        curr = node
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev