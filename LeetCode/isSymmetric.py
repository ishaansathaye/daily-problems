from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.flag = None

    def _isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''BFS Approach'''
        if root is None:
            return True
        # making this a stack makes this a dfs
        q = []  # of tree nodes
        q.append(root.left)
        q.append(root.right)
        while len(q) != 0:
            left = q.pop(0)
            right = q.pop(0)
            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False
            # into while check if left & right are not equal (consecutive vals)
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''Recursive Approach'''
        if root is None:
            return True
        self.flag = True
        self.dfs(root.left, root.right)
        return self.flag

    # can also do a boolean based recursion
    def dfs(self, left, right):
        if left is None and right is None:
            return
        if left is None or right is None or left.val != right.val:
            self.flag = False

        if self.flag:
            self.dfs(left.left, right.right)
            # st.pop
            self.dfs(left.right, right.left)
            # st.pop

        return (self.dfs(left.left, right.right) and
                self.dfs(left.right, right.left))
