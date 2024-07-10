from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.result = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.helper(root, self.result)
        return self.result

    def helper(self, root, currNum):  # can also make int-based recursion
        # base
        if root is None:
            return
            # return 0
        # logic
        currNum = currNum*10 + root.val  # keep adding node values until leaf
        # moving this if statement changes traversal type -> still works for all 3
        if root.left is None and root.right is None:
            self.result += currNum  # reached leaf -> add currNum to result
            # return currNum
        self.helper(root.left, currNum)
        # stack.pop()
        self.helper(root.right, currNum)
        # return case1 + case2
