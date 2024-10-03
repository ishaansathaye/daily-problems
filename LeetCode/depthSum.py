from typing import List
from collections import deque

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer,
        rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a
        nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds,
        if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds,
        if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.res = 0
        self.dfs(nestedList, 1)
        return self.res

    def dfs(self, nestedList, depth):
        for elem in nestedList:
            if elem.isInteger():
                self.res += depth*elem.getInteger()
            else:
                self.dfs(elem.getList(), depth+1)

    def depthSum1(self, nestedList: List[NestedInteger]) -> int:
        '''Int-Based Recursion'''
        return self.dfs(nestedList, 1)

    def dfs1(self, nestedList, depth):
        res = 0
        for elem in nestedList:
            if elem.isInteger():
                res += depth*elem.getInteger()
            else:
                res += self.dfs(elem.getList(), depth+1)
        return res

    def depthSum2(self, nestedList: List[NestedInteger]) -> int:
        '''Iterative Solution'''
        depth = 1
        st = deque()
        for elem in nestedList:
            st.append((elem, depth))

        res = 0
        while len(st) != 0:
            curr, currDepth = st.pop()
            if curr.isInteger():
                res += currDepth*curr.getInteger()
            else:
                for elem in curr.getList():
                    st.append((elem, currDepth+1))
        return res

    def depthSum3(self, nestedList: List[NestedInteger]) -> int:
        '''BFS'''
        depth = 1
        q = deque()
        for elem in nestedList:
            q.append(elem)

        res = 0
        while len(q) != 0:
            # processing level by level
            # increase depth when level is complete
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if curr.isInteger():
                    res += depth*curr.getInteger()
                else:
                    for elem in curr.getList():
                        q.append(elem)
            depth += 1
        return res
