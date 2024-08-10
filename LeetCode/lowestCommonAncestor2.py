# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pathP = None  # of Tree Nodes
        self.pathQ = None  # of Tree Nodes

    def _lowestCommonAncestor(self, root: 'TreeNode',
                              p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.backtrack(root, p, q, [])
        # compare the paths and find uncommon
        for i in range(len(self.pathP)):
            if self.pathP[i] != self.pathQ[i]:
                return self.pathP[i-1]
        return None

    def backtrack(self, root, p, q, path):
        # base
        if root is None:
            return
        # logic
        # action
        path.append(root)
        # can move around to change inorder, preorder, or postorder
        if root == p:
            self.pathP = path.copy()
            # append again to take care of leaf cases
            self.pathP.append(p)
        if root == q:
            self.pathQ = path.copy()
            self.pathQ.append(q)
        # recurse
        self.backtrack(root.left, p, q, path)
        # optimization of reducing rec calls:
        # if any is not found
        if self.pathP is None or self.pathQ is None:
            self.backtrack(root.right, p, q, path)
        # backtrack action
        path.pop(len(path)-1)

    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''Bottom Up Recursion'''
        # base
        if root is None or root == p or root == q:
            return root
        # logic
        left = self.lowestCommonAncestor(root.left, p, q)
        # st.pop()
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            # both children found so return root
            return root
        elif left is None and right is not None:
            # found in the right so return right root
            return right
        elif left is not None and right is None:
            # found in the left so return left root
            return left
        else:
            return None
