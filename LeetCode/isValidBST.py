from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.flag = True
        self.prev = None  # need this global to maintain passing into stack

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''Inorder Traversal of Binary Tree'''
        self.inorder(root)
        return self.flag
        # return inorder(root) for bool based recursion

    def inorder(self, root):
        if root is None:
            return

        # go all the way to the left side
        self.inorder(root.left)
        # left = self.inorder(root.left)

        # check if root is greater than prev
        # stack.pop()
        if self.prev is not None and self.prev.val >= root.val:
            self.flag = False
            # return False

        # set left to be the prev node
        self.prev = root

        if self.flag:  # saving rec calls by not going to right
            self.inorder(root.right)
        # if left is False: saving rec calls by not going to right
            # return False
        # right = self.inorder(root.right)
        # return left and right
