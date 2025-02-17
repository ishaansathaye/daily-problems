from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int,
                       right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head

        connections = right-left

        # set up to go to left node
        prev = None
        curr = head
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1

        # for connections after reversing
        # keep track of 1 before left node
        prevLeft = prev
        # keep track of the left node
        newTail = curr

        # reversing connections
        while connections >= 0:
            fast = curr.next
            curr.next = prev
            prev = curr
            curr = fast
            connections -= 1
        # at the end of while loop:
        # prev points to right node
        # curr points to after right node

        # for starting reverse with 1 case
        if prevLeft is not None:
            prevLeft.next = prev
        else:
            # reversing from beginning
            # so the end becomes the head
            head = prev

        # ammend connection of the reverse at start
        # the start of the reverse's next points to end
        newTail.next = curr

        return head


'''
1->2->3->4->5, left = 2, right = 4
=
1->4->3->2->5

connections = 2
1<-2->3->4->5
connections = 1
1<-2<-3->4->5
connections = 0
1<-2<-3<-4 5


1->2->3->4->5, left = 1, right = 3
connections = 2
None<-1->2->3->4->5
connections = 1
None<-1<-2->3->4->5
connection = 0
None<-1<-2<-3 4->5
3->2->1->4->5

newTail = 2
prevLeft = 1
-at end of reversing-
1.next re= 4 (prev)
2.next = 4 (curr)

'''

if __name__ == "__main__":
    def make_ll(arr):
        prevNode = None
        for i in range(len(arr)):
            newNode = ListNode()
            newNode.val = arr[i]
            if prevNode:
                prevNode.next = newNode
            else:
                head = newNode
            prevNode = newNode
        return head

    def print_ll(head):
        curr = head
        while curr is not None:
            print(curr.val, end="")
            curr = curr.next
        print()

    ll = make_ll([1, 2, 3, 4, 5])
    print_ll(ll)

    s = Solution()
    new_ll = s.reverseBetween(ll, 1, 3)
    print_ll(new_ll)
