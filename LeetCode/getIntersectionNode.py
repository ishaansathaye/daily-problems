# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''Own Solution'''
        pt1 = headA
        count1 = 0
        while pt1 is not None:
            pt1 = pt1.next
            count1 += 1
        
        pt2 = headB
        count2 = 0
        while pt2 is not None:
            pt2 = pt2.next
            count2 += 1
        
        pt1 = headA
        pt2 = headB
        if count1 > count2:
            diff = count1 - count2
            while diff != 0:
                pt1 = pt1.next
                diff -= 1
        else:
            diff = count2 - count1
            while diff != 0:
                pt2 = pt2.next
                diff -= 1
        
        while pt1 is not None and pt2 is not None:
            if pt1 == pt2:
                return pt1
            pt1 = pt1.next
            pt2 = pt2.next
        return None
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''s30 Solution'''
        lenA = 0
        curr = headA
        while curr is not None:
            curr = curr.next
            lenA += 1
        lenB = 0
        curr = headB
        while curr is not None:
            curr = curr.next
            lenB += 1
        
        p1 = headA
        p2 = headB
        while lenA > lenB:
            p1 = p1.next
            lenA -= 1
        while lenB > lenA:
            p2 = p2.next
            lenB -= 1

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p2