from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        self.dfs(root)
        return self.moves

    def dfs(self, root):
        # base
        if root is None:
            return 0
        # logic
        extraCoins = root.val - 1
        extraCoins += self.dfs(root.left)
        extraCoins += self.dfs(root.right)
        self.moves += abs(extraCoins)

        return extraCoins
