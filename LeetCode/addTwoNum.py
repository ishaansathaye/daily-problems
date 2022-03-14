# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # current_node1 = l1[0]
        # current_node2 = l2[0]
        # node = ListNode((current_node1.val+current_node2.val)%10)
        # final_node_list = [node]
        # max_length = max(len(l1), len(l2))
        # for i in range(max_length-1):
        #     add_value = (current_node1.val+current_node2.val)//10
        #     current_node1 = current_node1.next
        #     current_node2 = current_node2.next
        #     next_node_val = (add_value+current_node1.val+current_node2.val)%10
        #     node = ListNode(next_node_val)
        #     final_node_list[i].next = node
        #     final_node_list.append(node)
        # return final_node_list

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


