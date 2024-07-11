from typing import Optional, List


# definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        # global for optimized solution
        self.idx = 0  # idx for preorder
        self.hMap = {}  # map for inorder idx

    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        '''TC and SC: O(n^2)'''
        # base
        if len(preorder) == 0:
            return None
        # logic
        rootVal = preorder[0]  # find first root node
        root = TreeNode(rootVal)
        # find that root val in inorder arr
        rootIdx = -1  # root index in inorder arr
        for i in range(len(inorder)):  # Searching O(n)
            if inorder[i] == rootVal:
                rootIdx = i
                break

        inorderLeft = inorder[0:rootIdx]  # O(n)
        inorderRight = inorder[rootIdx+1:len(inorder)]
        preLeft = preorder[1:1+len(inorderLeft)]
        preRight = preorder[1+len(inorderLeft):len(preorder)]

        # build left subtree
        root.left = self.buildTree(preLeft, inorderLeft)
        # build right subtree
        root.right = self.buildTree(preRight, inorderRight)
        return root

    def buildTree2(self, preorder: List[int],
                   inorder: List[int]) -> Optional[TreeNode]:
        '''Optimized Time and Space for both O(n)'''
        # base
        if len(preorder) == 0:
            return None
        # logic
        # create hash map with value and index from inorder
        for i in range(len(inorder)):
            self.hMap[inorder[i]] = i

        return self.helper(preorder, 0, len(inorder)-1)

    def helper(self, preorder, start, end):
        # base
        if start > end:  # if cross then null
            return None

        # logic
        rootVal = preorder[self.idx]  # get root value with global idx
        root = TreeNode(rootVal)

        self.idx += 1  # increase preorder idx (go to next root)
        rootIdx = self.hMap[rootVal]  # inorder array idx of root

        # make bounds for subtrees:
        root.left = self.helper(preorder, start, rootIdx - 1)
        root.right = self.helper(preorder, rootIdx+1, end)

        return root
