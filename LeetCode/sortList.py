from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Original Solution - O(nlogn), O(n)'''
        if not head:
            return head
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        res.sort()
        prev = None
        head = None
        for n in res:
            if head is None:
                head = ListNode(n)
                prev = head
            else:
                curr = ListNode(n)
                prev.next = curr
                prev = curr
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Top-Down Merge Sort: O(nlogn), O(logn)'''
        # single node or no node
        if not head or not head.next:
            return head

        mid = self.getMid(head)
        # from head to prev middle
        left = self.sortList(head)
        # from middle to end
        right = self.sortList(mid)

        # merge
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        # link rest of unfinished list
        if left:
            tail.next = left
        else:
            tail.next = right
        return dummy.next

    def getMid(self, head):
        '''Fast and Slow Pointer'''
        slow = None
        fast = head
        while fast and fast.next:
            if not slow:
                slow = fast
            else:
                # slow moves 1 step
                slow = slow.next
            # fast moves 2 steps
            fast = fast.next.next
        # slow positioned before middle of list
        mid = slow.next
        # break list by setting prev middle's next to None
        slow.next = None
        return mid

    def bt_sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Bottom-Up Merge Sort: O(nlogn), O(1)'''
        if head is None or head.next is None:
            return head
        # get length of list
        n = self.getLength(head)
        start = head
        dummy = ListNode()
        size = 1
        while size < n:
            self.tail = dummy
            while start is not None:
                # only 1 segment
                if start.next is None:
                    # attach it to the tail of original
                    self.tail.next = start
                    break
                # get mid given size
                mid = self.split(start, size)
                # merge both lists
                self.merge2(start, mid)
                # go the next list
                start = self.nextList
            start = dummy.next
            size *= 2
        return dummy.next

    def merge2(self, list1, list2):
        dummy = ListNode()
        newTail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                newTail.next = list1
                list1 = list1.next
            else:
                newTail.next = list2
                list2 = list2.next
            newTail = newTail.next
        if list1:
            newTail.next = list1
        else:
            newTail.next = list2

        # go to end of merged list
        while newTail.next:
            newTail = newTail.next
        # make links between old tail and head of merged list
        # original list -> merged list
        self.tail.next = dummy.next
        # update old tail to new tail
        self.tail = newTail

    def split(self, start, size):
        # using slow-fast pointers to find middle and end
        slow = start
        fast = start.next
        for i in range(1, size):
            # fast by 2 or by 1 if 2nd is None
            if fast and fast.next:
                fast = fast.next.next
            else:
                if fast:
                    fast = fast.next
            if slow.next:
                slow = slow.next
        # get mid
        mid = slow.next
        # sever links to split list
        slow.next = None
        # get end of list
        if fast:
            self.nextList = fast.next
        else:
            self.nextList = None
        # sever links with next list
        if fast:
            fast.next = None
        return mid

    def getLength(self, head):
        i = 0
        start = head
        while start:
            start = start.next
            i += 1
        return i
