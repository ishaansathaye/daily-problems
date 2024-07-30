from typing import Optional, List
import heapq as hq

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists:
                    List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []  # pq of ListNode
        for i in range(len(lists)):
            if lists[i] is not None:
                hq.heappush(pq, (lists[i].val, i, lists[i]))

        dummy = ListNode(-1)
        curr = dummy
        i = 0
        while len(pq) != 0:  # O(N) -> all elements going into pq
            _, i, minNode = hq.heappop(pq)  # O(log k)
            curr.next = minNode
            curr = curr.next
            if minNode.next is not None:
                hq.heappush(pq, (minNode.next.val, i,
                            minNode.next))  # O(log k)
        curr.next = None

        return dummy.next

    def _mergeKLists(self, lists:
                     List[Optional[ListNode]]) -> Optional[ListNode]:
        '''Merging of Lists (no heap)'''
        merged = ListNode(-2**31)  # dummy of -inf
        for head in lists:
            if head is not None:
                merged = self.merge(merged, head)  # new merged list
        return merged.next

    def merge(self, head1, head2):
        '''Merging 2 Linked Lists'''
        dummy = ListNode(-1)
        curr = dummy
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next

        # one list is not finished
        if head1 is not None:
            curr.next = head1
        # other list is not finished
        if head2 is not None:
            curr.next = head2

        return dummy.next
