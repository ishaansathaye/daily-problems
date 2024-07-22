from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''BFS: O(n), O(n)'''
        result = []
        if root is None:
            return result
        queue = []
        queue.append(root)
        while len(queue) != 0:
            maxN = -2**31
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                if curr.val > maxN:
                    maxN = curr.val
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            result.append(maxN)
        return result

    def _largestValues(self, root: Optional[TreeNode]) -> List[int]:
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
        if len(result) == level:
            # add min value at that level (start)
            result.append(-2**31)
        if root.val > result[level]:
            result[level] = root.val
        # left call
        self.dfs(root.left, level+1, result)
        # right call
        self.dfs(root.right, level+1, result)
