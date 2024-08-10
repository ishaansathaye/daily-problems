from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect0(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''BFS with Q'''
        if root is None:
            return None
        q = []
        q.append(root)
        while len(q) != 0:
            size = len(q)  # where does the level end
            for i in range(size):
                curr = q.pop(0)
                # if not the last node
                if i != size-1:
                    curr.next = q[0]
                # put the children in q
                if curr.left is not None:
                    q.append(curr.left)
                    # perfect bt:
                    q.append(curr.right)
        return root

    def _connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''Optimal BFS and LL; O(1) Space'''
        if root is None:
            return None
        level = root
        while level.left is not None:
            # process a level
            curr = level
            while curr is not None:
                # join left and right of root
                curr.left.next = curr.right
                if curr.next is not None:
                    # join root's children (right child -> left child)
                    curr.right.next = curr.next.left
                curr = curr.next
            level = level.left
        return root

    def connect1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''DFS'''
        if root is None:
            return None
        self.dfs(root)
        return root

    def dfs(self, root):
        # base case
        if root.left is None:
            return
        # logic
        root.left.next = root.right
        # preorder (can also do inorder)
        if root.next is not None:
            root.right.next = root.next.left
        self.dfs(root.left)
        self.dfs(root.right)

    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''DFS with Left and Right'''
        if root is None:
            return None
        self.dfs(root.left, root.right)
        return root

    def _dfs(self, left, right):
        # base case
        if left is None:
            return
        # logic
        left.next = right
        self._dfs(left.left, left.right)
        self._dfs(left.right, right.left)
        self._dfs(right.left, right.right)
