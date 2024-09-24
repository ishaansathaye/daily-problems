from typing import Optional
from collections import defaultdict

# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''2 Pass Algo'''
        if head is None:
            return None
        hMap = defaultdict()
        copyHead = Node(head.val)
        hMap[head] = copyHead
        # pointers in each list
        curr = head
        copyCurr = copyHead

        # making next links
        while curr.next is not None:
            # handle the next pointer
            copyNode = Node(curr.next.val)
            hMap[curr.next] = copyNode
            copyCurr.next = copyNode
            # next
            curr = curr.next
            copyCurr = copyCurr.next

        # making random pointers
        curr = head
        copyCurr = copyHead
        while curr is not None:
            if curr.random is not None:
                copyCurr.random = hMap[curr.random]
            # next
            curr = curr.next
            copyCurr = copyCurr.next

        return copyHead

    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''1 Pass Algo'''
        if head is None:
            return None
        hMap = defaultdict()
        copyHead = Node(head.val)
        hMap[head] = copyHead
        # pointers in each list
        curr = head
        copyCurr = copyHead

        # making next links
        while curr is not None:
            # handle the next pointer
            copyCurr.next = self.clone(curr.next, hMap)
            # random pointer
            copyCurr.random = self.clone(curr.random, hMap)
            # next
            curr = curr.next
            copyCurr = copyCurr.next

        return copyHead

    def clone(self, node, hMap):
        if node is None:
            return None
        if node in hMap:
            return hMap[node]
        newNode = Node(node.val)
        hMap[node] = newNode
        return newNode

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''3 Pass - Constant Space'''
        if head is None:
            return None
        # create the deep copy
        # put it next original
        curr = head
        while curr is not None:
            copyCurr = Node(curr.val)
            copyCurr.next = curr.next
            curr.next = copyCurr
            # move it by twice (skip copy)
            curr = curr.next.next

        # handle random pointers
        curr = head
        while curr is not None:
            if curr.random is not None:
                # deep copy right next to random
                curr.next.random = curr.random.next
            curr = curr.next.next

        # separate out lists
        curr = head
        copyCurr = curr.next
        copyHead = copyCurr
        while curr is not None:
            curr.next = curr.next.next
            if copyCurr.next is not None:
                copyCurr.next = copyCurr.next.next
            curr = curr.next
            copyCurr = copyCurr.next

        return copyHead
