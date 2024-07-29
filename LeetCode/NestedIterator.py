'''Non-LAZY LOADING SOLUTION'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.i = 0  # pointer
        self.li = []
        self.dfs(nestedList)

    def dfs(self, nestedList):
        # no base case - for loop takes care of it
        # logic
        for el in nestedList:
            if el.isInteger():
                self.li.append(el.getInteger())
            else:
                self.dfs(el.getList())

    def next(self) -> int:
        re = self.li[self.i]
        self.i += 1
        return re

    def hasNext(self) -> bool:
        if self.i == len(self.li):
            return False
        return True


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
