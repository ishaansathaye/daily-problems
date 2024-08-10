from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''With Stack'''
        if root is None:
            return None
        st = []
        res = []
        while len(st) != 0 or root is not None:
            # same as inorder(root.left)
            while root is not None:
                st.append(root)
                root = root.left
            root = st.pop()
            res.append(root.val)
            root = root.right

        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''Morris Traversal: Without Stack'''
        '''Asked for covnerting BST into Linked List'''
        if root is None:
            return None
        res = []
        while root is not None:
            if root.left is None:
                res.append(root.val)
                root = root.right
            else:
                pred = root.left
                while pred.right is not None and pred.right is not root:
                    pred = pred.right
                if pred.right is None:
                    # Downward Motion
                    # set right of pred to the next elem (root)
                    pred.right = root
                    root = root.left
                else:
                    # Upward Motion
                    pred.right = None
                    # Putting root in
                    res.append(root.val)
                    root = root.right
        return res
