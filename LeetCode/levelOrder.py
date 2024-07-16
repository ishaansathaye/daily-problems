from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = []  # of tree nodes
        queue.append(root)
        while len(queue) != 0:
            size = len(queue)
            li = []
            # how many elements at that level
            for i in range(size):
                curr = queue.pop(0)
                li.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            result.append(li)
        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''DFS Approach -> TC: O(n), SC: O(1)'''
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
            # make sure list is there at that level
            result.append([])
        result[level].append(root.val)
        # left call
        self.dfs(root.left, level+1, result)
        # right call
        self.dfs(root.right, level+1, result)
