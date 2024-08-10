from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = None
        self.count = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''Recursive In Order'''
        self.count = k
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        # root
        self.count -= 1
        if self.count == 0:
            self.res = root.val
            # self.flag = True
            return
        # or can check if flag has been set and not do right side
        self.inorder(root.right)
