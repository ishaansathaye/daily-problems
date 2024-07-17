from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.x_parent = None
        self.x_depth = None
        self.y_parent = None
        self.y_depth = None

    def _isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        '''DFS Approach'''
        '''Can also put a Parent Check of BFS here'''
        # null check
        self.dfs(root, None, x, y, 0)
        return self.x_parent != self.y_parent and self.x_depth == self.y_depth

    def dfs(self, root, parent, x, y, level):
        # base
        if root is None:
            return
        if root.val == x:
            self.x_parent = parent
            self.x_depth = level
        if root.val == y:
            self.y_parent = parent
            self.y_depth = level
        # logic
        self.dfs(root.left, root, x, y, level+1)
        # do dfs if either x is not found or y is not found
        if self.x_parent is None or self.y_parent is None:
            self.dfs(root.right, root, x, y, level+1)

    def __isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        '''BFS Approach with Parent Queue'''
        # null check
        q = []
        pq = []  # parent queue
        q.append(root)
        pq.append(None)
        px = None  # parent of x
        py = None  # parent of y
        while len(q) != 0:
            size = len(q)
            for i in range(size):  # go over the level
                curr = q.pop(0)
                pcurr = pq.pop(0)
                if curr.val == x:
                    px = pcurr
                if curr.val == y:
                    py = pcurr

                if curr.left is not None:
                    q.append(curr.left)
                    pq.append(curr)
                if curr.right is not None:
                    q.append(curr.right)
                    pq.append(curr)
            if px is not None and py is not None:  # check if both found
                return px != py
            if px is not None or py is not None:
                return False
        return False

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        '''BFS Approach with Parent Check'''
        # null check
        q = []
        q.append(root)
        px = None  # parent of x
        py = None  # parent of y
        while len(q) != 0:
            size = len(q)
            for i in range(size):  # go over the level
                curr = q.pop(0)
                if curr.left is not None:
                    if curr.left.val == x:
                        px = curr.val
                    if curr.left.val == y:
                        py = curr.val
                    q.append(curr.left)
                if curr.right is not None:
                    if curr.right.val == x:
                        px = curr.val
                    if curr.right.val == y:
                        py = curr.val
                    q.append(curr.right)
                if px is not None and py is not None:
                    if px == py:
                        return False
                    else:
                        return True
            if px is not None or py is not None:
                return False
        return False
