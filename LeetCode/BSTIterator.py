# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class BSTIterator:
#     '''NOT ACCEPTED in INTERVIEW; Design Problem'''
#     def __init__(self, root: Optional[TreeNode]):
#         self.li = []
#         self.idx = 0
#         self.inorder(root)
    
#     def inorder(self, root): # O(n)
#         if root is None:
#             return
#         self.inorder(root.left)
#         self.li.append(root)
#         self.inorder(root.right)

#     def next(self) -> int: # O(1)
#         re = self.li[self.idx].val
#         self.idx += 1
#         return re

#     def hasNext(self) -> bool: # O(1)
#         if self.idx != len(self.li):
#             return True
#         return False

class BSTIterator:
    '''Controlled Recursion'''
    
    def __init__(self, root: Optional[TreeNode]):
        self.st = [] # of TreeNode
        self.dfs(root)
        
    def dfs(self, root): # not a recursive function
        while root is not None:
            self.st.append(root)
            root = root.left # dfs all the way to left

    def next(self) -> int: # O(h) in the worst class (height of tree)
        # avg/amortized is O(1)
        popped = self.st.pop()
        self.dfs(popped.right) # once popped do dfs on its right side
        return popped.val

    def hasNext(self) -> bool: # O(1)
        return len(self.st) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()