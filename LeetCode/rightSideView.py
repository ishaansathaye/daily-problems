from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''BFS: O(n), O(n)'''
        result = []
        if root is None:
            return result
        q = []  # of type Tree Nodes
        q.append(root)
        while len(q) != 0:
            size = len(q)  # take size of queue
            # processing level
            for i in range(size):
                curr = q.pop(0)
                # left side view is if i == 0
                if i == size - 1:  # if last element of level
                    result.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
        return result

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''DFS: O(n), O(h)'''
        result = []
        if root is None:
            return result
        self.dfs(root, 0, result)
        return result

    def dfs(self, root, level, result):
        # base
        if root is None:
            return
        # logic
        # result does not have element at that level then add it
        if len(result) == level:
            result.append(root.val)
        self.dfs(root.right, level+1, result)
        self.dfs(root.left, level+1, result)
