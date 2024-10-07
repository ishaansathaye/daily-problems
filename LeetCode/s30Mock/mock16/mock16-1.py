from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode],
                      startValue: int, destValue: int) -> str:
        '''TC: O(n), SC: O(n)'''
        pathStart = []
        pathDest = []
        self.dfs(root, startValue, pathStart)
        self.dfs(root, destValue, pathDest)

        # find lca using paths
        i = 0
        finalPath = []
        # finding which are common letters to find lca starting
        while (i < len(pathStart) and i < len(pathDest)
               and pathStart[i] == pathDest[i]):
            i += 1
        # add Us for how many to reach lca
        finalPath = ['U']*(len(pathStart)-i)
        # append path for lca to dest for final
        for j in range(i, len(pathDest)):
            finalPath.append(pathDest[j])
        return ''.join(finalPath)

    def dfs(self, root, target, path):
        # base
        if root is None:
            return False

        if root.val == target:
            return True

        # logic
        path.append('L')
        if self.dfs(root.left, target, path):
            return True
        # not found -> backtrack
        path.pop(len(path)-1)
        path.append('R')
        if self.dfs(root.right, target, path):
            return True
        path.pop(len(path)-1)
        # not found
        return False
