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

    def rangePreOrder(self, root) -> bool:
        '''Using Range in Recursion and Preorder Traversal'''
        self.flag = True
        self.helper(root, None, None)
        return self.flag

    def helper(self, root, min, max):  # Time: O(n) Space: O(h)
        # base
        if root is None:
            return
        # logic
        # moving these if statements in between calls -> in order traversal
        # moving these after calls -> post order traversal
        if min is not None and root.val <= min:
            # not None for checking if infinity
            self.flag = False
            # return False
        if max is not None and root.val >= max:
            self.flag = False
            # return False
        # going to left use parent's min and max as parent's val
        self.helper(root.left, min, root.val)
        # right = above statement
        # stack.pop()
        # if left is False:
        # return False
        # going to right use parent's val as min and parent's max val
        self.helper(root.right, root.val, max)
        # right = above statement
        # return left and right
