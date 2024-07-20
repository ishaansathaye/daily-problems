from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if (abs(self.height(root.left) - self.height(root.right)) > 1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        '''Finding Max Height of each Subtree'''
        # base
        if root is None:
            return 0
        # logic
        return max(self.height(root.left), self.height(root.right)) + 1
