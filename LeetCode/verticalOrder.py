from typing import List, Optional
from collections import defaultdict, deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''BFS Solution'''
        if root is None:
            return None
        hMap = defaultdict(list)
        q = deque()
        q.append((root, 0))
        minC = 0
        maxC = 0
        while len(q) != 0:
            p = q.popleft()
            curr = p[0]
            col = p[1]
            # if col not in hMap:
            #     hMap[col] = []
            hMap[col].append(curr.val)
            # process children
            if curr.left is not None:
                q.append((curr.left, col-1))
                minC = min(minC, col-1)
            if curr.right is not None:
                q.append((curr.right, col+1))
                maxC = max(maxC, col+1)

        # Bucket sort on the hash map
        res = []
        for i in range(minC, maxC+1):
            res.append(hMap[i])

        return res
