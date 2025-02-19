from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''Simple BFS'''
        res = []
        if not root:
            return res
        dirs = 0
        q = deque()
        q.append(root)

        while len(q) != 0:
            size = len(q)
            # can also make temp deque
            # solution then similar to #2 solution
            # appendleft vs append when direction changes
            temp = []
            for i in range(size):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if not dirs:
                res.append(temp.reverse())
            else:
                res.append(temp)
            dirs = not dirs
        return res

    def _zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''BFS with 1 Loop'''
        res = []
        if root is None:
            return res
        # None means a level has been finished
        nq = deque([root, None])
        dirs = True

        # instead of arr for temp
        # make deque so append from both sides
        # for zigzag ordering
        temp = deque()
        while len(nq) > 0:
            curr = nq.popleft()

            if curr:
                if dirs:
                    temp.append(curr.val)
                else:
                    # adding at the beginning of q
                    temp.appendleft(curr.val)

                if curr.left:
                    nq.append(curr.left)
                if curr.right:
                    nq.append(curr.right)
            else:
                # level has been finished
                res.append(list(temp))
                # mark a new level
                if len(nq) > 0:
                    nq.append(None)
                # start next level
                temp = deque()
                dirs = not dirs

        return res

    def _DFSzigzagLevelOrder(self, root:
                             Optional[TreeNode]) -> List[List[int]]:
        '''DFS: Level-Order Approach'''
        res = []
        if not root:
            return res
        self.dfs(root, 0, res)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res

    def dfs(self, root, level, res):
        # base case
        if not root:
            return

        # logic
        if len(res) <= level:
            # ensure a list exists already at that level
            res.append(deque([root.val]))
        else:
            # alternate bewteen order bsaed on odd or even level
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].appendleft(root.val)
        # left call
        self.dfs(root.left, level+1, res)
        # right call
        self.dfs(root.right, level+1, res)
