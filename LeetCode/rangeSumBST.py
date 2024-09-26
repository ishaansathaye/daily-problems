from collections import deque
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode],
                    low: int, high: int) -> int:
        '''BFS'''
        q = deque()
        q.append(root)
        res = 0
        while len(q) != 0:
            curr = q.popleft()
            if curr.val >= low and curr.val <= high:
                res += curr.val
            # left
            if curr.val >= low and curr.left is not None:
                q.append(curr.left)
            # right
            if curr.val <= high and curr.right is not None:
                q.append(curr.right)
        return res

    def rangeSumBST1(self, root: Optional[TreeNode],
                     low: int, high: int) -> int:
        '''DFS'''
        self.res = 0
        self.helper(root, low, high)
        return self.res

    def helper(self, root, low, high):
        # base
        if root is None:
            return
        # logic
        # pre order (can do inorder or postorder)
        if root.val >= low and root.val <= high:
            self.res += root.val
        # left
        if root.val > low:
            self.helper(root.left, low, high)
        # right
        if root.val < high:
            self.helper(root.right, low, high)

    def rangeSumBST2(self, root: Optional[TreeNode],
                     low: int, high: int) -> int:
        '''Int Based Recursion'''
        return self.helper2(root, low, high)

    def helper2(self, root, low, high):
        # base
        if root is None:
            return 0
        # logic
        res = 0
        if root.val >= low and root.val <= high:
            res += root.val
        if root.val > low:
            res += self.helper2(root.left, low, high)
        if root.val < high:
            res += self.helper2(root.right, low, high)
        return res

    def rangeSumBST3(self, root: Optional[TreeNode],
                     low: int, high: int) -> int:
        '''Iterative Preorder Traversal'''
        st = deque()
        # pre order
        st.append(root)
        res = 0
        while len(st) != 0:
            curr = st.pop()
            if curr.val >= low and curr.val <= high:
                res += curr.val
            # LIFO so left comes out first (mirrors q)
            if curr.val < high and curr.right is not None:
                st.append(curr.right)
            if curr.val > low and curr.left is not None:
                st.append(curr.left)
        return res

    def rangeSumBST4(self, root: Optional[TreeNode],
                     low: int, high: int) -> int:
        '''Inorder Traversal'''
        st = deque()
        res = 0
        while len(st) != 0 or root is not None:
            # going left here
            while root is not None:
                st.append(root)
                if root.val < low:
                    break
                root = root.left
            root = st.pop()
            if root.val >= low and root.val <= high:
                res += root.val
            if root.val < high:
                root = root.right
            else:
                root = None
        return res

    def rangeSumBST5(self, root: Optional[TreeNode],
                     low: int, high: int) -> int:
        '''Postorder Traversal'''
        st = deque()
        res = 0
        st.append(root)
        prev = None
        while len(st) != 0:
            curr = st[-1]
            if prev is None or prev.left == curr or prev.right == curr:
                if curr.left is not None:
                    st.append(curr.left)
                elif curr.right is not None:
                    st.append(curr.right)
                else:
                    # process root
                    if curr.val >= low and curr.val <= high:
                        res += curr.val
                    st.pop()
            elif curr.left == prev:
                if curr.right is not None:
                    st.append(curr.right)
                else:
                    # process root
                    if curr.val >= low and curr.val <= high:
                        res += curr.val
                    st.pop()
            elif curr.right == prev:
                # process root
                if curr.val >= low and curr.val <= high:
                    res += curr.val
                st.pop()
            prev = curr
        return res
