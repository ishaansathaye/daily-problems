from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''Recursive Solution: Pre-order Traversal'''
        self.dfs(root)

    def dfs(self, root):
        if root is None:
            return None

        # leaf node so just return that node
        if not root.left and not root.right:
            return root

        # traverse left subtree
        leftSubtreeNode = self.dfs(root.left)

        # traverse right subtree
        rightSubtreeNode = self.dfs(root.right)

        # make connections for the leftSubtree
        # remove left connection to None
        if leftSubtreeNode:
            # 3 -> 4
            leftSubtreeNode.right = root.right
            # 2 -> 3
            root.right = root.left
            root.left = None

        # Return tail of the flattened subtree
        if rightSubtreeNode:
            return rightSubtreeNode
        return leftSubtreeNode

    prev = None

    def _flatten(self, root: Optional[TreeNode]) -> None:
        '''Recursive Solution: Post-order Traversal'''
        if root is None:
            return

        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root

    def mflatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''Morris Traversal: O(1) Space'''
        if not root:
            return None

        node = root
        while node is not None:
            if node.left:
                # find rightmost node of left subtree
                # (almost rightmost node)
                rightMost = node.left
                while rightMost.right is not None:
                    rightMost = rightMost.right

                # make the correct connections
                rightMost.right = node.right
                node.right = node.left
                node.left = None

            # go to right subtree
            # node.right is changed after connections are made
            node = node.right
