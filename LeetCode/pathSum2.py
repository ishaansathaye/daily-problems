from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []

    def pathSum(self, root: Optional[TreeNode],
                targetSum: int) -> List[List[int]]:
        self.helper(root, 0, targetSum, [])
        return self.result

    def helper(self, root, curSum, targetSum, curList):
        # base case
        if root is None:
            return

        # logic
        curSum += root.val
        # create new list to address pass by reference problem
        copyPath = curList.copy()
        copyPath.append(root.val)

        # check if leaf node
        if root.left is None and root.right is None:
            if curSum == targetSum:
                self.result.append(copyPath)
            return

        # can also create deep copy in both calls:
        self.helper(root.left, curSum, targetSum, copyPath)
        # stack.pop()
        self.helper(root.right, curSum, targetSum, copyPath)
        # stack.pop()

    def helper2(self, root, curSum, targetSum, curList):
        '''Backtracking Technique'''
        # base case
        if root is None:
            return
        # logic
        curSum += root.val
        curList.append(root.val)  # O(1)
        # check if leaf node
        if root.left is None and root.right is None:
            if curSum == targetSum:
                # need to create a deep copy
                # if not then empty lists added
                # since by reference
                self.result.append(list(curList))
        self.helper(root.left, curSum, targetSum, curList)
        # stack.pop()
        self.helper(root.right, curSum, targetSum, curList)
        # stack.pop()

        # backtrack
        curList.pop()
