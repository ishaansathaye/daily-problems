# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _lowestCommonAncestor(self, root: 'TreeNode',
                              p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''TC: O(h), SC: Rec Stack'''
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''TC: O(h), SC: O(1)'''
        while True:
            if root.val > p.val and root.val > q.val:
                # greater than both then go the left side
                root = root.left
            elif root.val < p.val and root.val < q.val:
                # less than both go to right side
                root = self.lowestCommonAncestor(root.right, p, q)
            else:
                # in between both then it is the LCA
                # or it is equal to one of them then return itself
                return root
