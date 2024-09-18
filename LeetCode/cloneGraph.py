from typing import Optional
from collections import defaultdict
import deque

# Definition for a Node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''BFS'''
        if node is None:
            return None
        q = deque()  # type Node
        # for visited and associations
        hMap = defaultdict(Node)
        copyNode = Node(node.val)
        hMap[node] = copyNode
        q.append(node)
        while len(q) != 0:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in hMap:
                    # create deep copy
                    newNode = Node(n.val)
                    hMap[n] = newNode
                    q.append(n)
                # put the deep copy of this neighbor in list
                # of original's nodes deep copy
                hMap[curr].neighbors.append(hMap[n])
        return copyNode

    def _cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''DFS'''
        if node is None:
            return None
        hMap = defaultdict(Node)
        self.dfs(node, hMap)
        return hMap[node]

    def dfs(self, node, hMap):
        # base
        if node in hMap:
            return
        # logic
        newNode = Node(node.val)
        hMap[node] = newNode
        for n in node.neighbors:
            self.dfs(n, hMap)
            hMap[node].neighbors.append(hMap[n])
