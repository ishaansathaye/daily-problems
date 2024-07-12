from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.hMap = {}
        self.idx = 0  # index on post order array

    def buildTree(self, inorder: List[int],
                  postorder: List[int]) -> Optional[TreeNode]:
        self.idx = len(postorder) - 1

        for i in range(len(inorder)):
            self.hMap[inorder[i]] = i

        return self.helper(postorder, 0, len(inorder)-1)

    # left -- right -- root for postorder
    def helper(self, postorder, start, end):
        # base
        if start > end:
            return None
        # logic
        rootVal = postorder[self.idx]
        self.idx -= 1
        root = TreeNode(rootVal)
        rootIdx = self.hMap[rootVal]

        # right fist
        root.right = self.helper(postorder, rootIdx+1, end)
        # left
        root.left = self.helper(postorder, start, rootIdx-1)

        return root
