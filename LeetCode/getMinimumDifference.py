from typing import Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''BFS: Level Order Traversal - O(nlogn)'''
        q = deque()
        minDiff = 2**31
        q.append(root)
        res = []

        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        res.sort()
        i = 0
        for j in range(1, len(res)):
            minDiff = min(minDiff, abs(res[i] - res[j]))
            i += 1
        return minDiff

    def _getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''BFS: In Order Traversal - O(n)'''
        st = []
        minDiff = 2**31
        res = []

        while len(st) != 0 or root is not None:
            while root is not None:
                st.append(root)
                root = root.left
            root = st.pop()
            res.append(root.val)
            root = root.right

        i = 0
        for j in range(1, len(res)):
            minDiff = min(minDiff, abs(res[i] - res[j]))
            i += 1
        return minDiff

    def dfs_getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''DFS: In Order Traversal - O(n) with list'''
        res = []
        minDiff = 2**31
        self.dfs(root, res)
        i = 0
        for j in range(1, len(res)):
            minDiff = min(minDiff, abs(res[i] - res[j]))
            i += 1
        return minDiff

    def dfs(self, node, res):
        if node is None:
            return
        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)

    def dfs2_getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''DFS: In Order Traversal - O(n) with no list'''
        self.minDiff = 2**31
        self.prevNode = None
        self.dfs2(root)
        return self.minDiff

    def dfs2(self, root):
        if root is None:
            return
        self.dfs2(root.left)
        if self.prevNode:
            self.minDiff = min(self.minDiff, abs(self.prevNode.val - root.val))
        self.prevNode = root
        self.dfs2(root.right)
