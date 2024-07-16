# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get middle
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # reverse
        fast = self.reverse(slow.next)
        slow.next = None
        slow = head

        # traverse one to check
        while fast is not None:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
    
    def reverse(self, node):
        prev = None
        curr = node
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev