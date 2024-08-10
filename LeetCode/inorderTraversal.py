from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
