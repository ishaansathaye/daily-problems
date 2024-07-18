from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def __init__(self):
        self.result = 0

    def _getImportance(self, employees: List['Employee'], id: int) -> int:
        '''BFS'''
        hMap = {}  # of type integer : employee object
        q = []  # of id or employee objects (id better)
        for e in employees:
            hMap[e.id] = e

        result = 0
        q.append(id)
        while len(q) != 0:
            currId = q.pop(0)
            e = hMap[currId]
            result += e.importance
            # iterate over subs
            for subId in e.subordinates:
                q.append(subId)
        return result

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        '''Void Based DFS'''
        hMap = {}
        for e in employees:
            hMap[e.id] = e

        self.dfs(hMap, id)
        return self.result

    def dfs(self, hMap, id) -> None:
        # base
        # logic
        e = hMap[id]
        self.result += e.importance
        for subId in e.subordinates:
            self.dfs(hMap, subId)
