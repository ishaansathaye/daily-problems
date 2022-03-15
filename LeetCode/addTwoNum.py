# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #107 ms
        l1_num = ""
        while l1 != None:
            l1_num += str(l1.val)
            l1 = l1.next
        l2_num = ""
        while l2 != None:
            l2_num += str(l2.val)
            l2 = l2.next
        final_num = str(int(l1_num[::-1]) + int(l2_num[::-1]))[::-1]
        node_list = []
        head = None
        for i in range(len(final_num)):
            if head != None:
                node = ListNode(final_num[i])
                head.next = node
                head = node
                node_list.append(node)
            else:
                node = ListNode(final_num[i])
                head = node
                node_list.append(node)
        return node_list[0]

    #Alternate - 68ms
    def addTwoNumbersAlt(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                    
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result.next

    #Can also create multiple functions for the main function to use
    def to_int(l: ListNode):
        s = ''
        while l != None:
            s += str(l.val)
            l = l.next
        return int(s[::-1])
    
    def to_list(n: int):
        s = str(n)[::-1]
        head = prev = None
        for ch in s:
            node = ListNode(int(ch))
            if prev is not None:
                prev.next = node
            prev = node
            if head is None:
                head = prev
        return head
    
    def addTwoNumbersAlt2(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = Solution.to_int(l1)
        b = Solution.to_int(l2)
        return Solution.to_list(a + b)


# node3 = ListNode(3)
# node2 = ListNode(4, node3)
# node1 = ListNode(2, node2)
# l1 = node1

# node6 = ListNode(4)
# node5 = ListNode(6, node6)
# node4 = ListNode(5, node5)
# l2 = node4

node3 = ListNode(9)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)
l1 = node1

node7 = ListNode(9)
node6 = ListNode(4, node7)
node5 = ListNode(6, node6)
node4 = ListNode(5, node5)
l2 = node4

temp = Solution()
returned_node_list = temp.addTwoNumbers(l1, l2)
print(returned_node_list.val)
# for i in returned_node_list:
#     print(i.val)


