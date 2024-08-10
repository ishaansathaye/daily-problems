from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = None
        self.flag = False

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        # swap values
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp

    def inorder(self, root):
        # base
        if root is None:
            return
        # logic
        self.inorder(root.left)

        # process root
        if self.prev is not None and self.prev.val >= root.val:
            if not self.flag:
                # first breach
                self.first = self.prev
                self.second = root
                self.flag = True
            else:
                # second breach
                self.second = root
        self.prev = root
        # can save by putting flag here
        # replace earlier flag with just if first is None
        self.inorder(root.right)
