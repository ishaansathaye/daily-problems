from typing import List


class Solution:
    def __init__(self):
        self.path = None
        self.visited = None
        self.hMap = None

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        '''BFS Topological Manner'''
        hMap = {}  # integer and list of dependents on integer
        inDegrees = [0 for i in range(numCourses)]  # length is num of courses

        for pre in prerequisites:
            inD = pre[0]  # dependent
            out = pre[1]  # indep
            inDegrees[inD] += 1
            if out not in hMap:
                hMap[out] = []
            # add deps to the indep key
            hMap[out].append(inD)

        # iterate over inDegrees arr
        queue = []  # of integers
        count = 0  # how many elem in queue
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)
                count += 1

        # all the courses are done
        if count == numCourses:
            return True
        # nothing has gone in the queue
        if count == 0:
            return False

        # bfs
        while len(queue) != 0:
            parent = queue.pop(0)  # parent out queue
            if parent in hMap:
                children = hMap[parent]  # get children
                for child in children:
                    inDegrees[child] -= 1
                    # once indegree is 0 then put into queue
                    if inDegrees[child] == 0:
                        queue.append(child)
                        count += 1
                        if count == numCourses:
                            return True
        return False

    def _canFinish(self, numCourses: int,
                   prerequisites: List[List[int]]) -> bool:
        '''DFS'''
        self.hMap = {}  # integer and list of dependents on integer
        self.path = [False for i in range(numCourses)]
        self.visited = [False for i in range(numCourses)]
        inDegrees = [0 for i in range(numCourses)]  # length is num of courses

        for pre in prerequisites:
            inD = pre[0]  # dependent
            out = pre[1]  # indep
            inDegrees[inD] += 1
            if out not in self.hMap:
                self.hMap[out] = []
            # add deps to the indep key
            self.hMap[out].append(inD)

        for i in range(numCourses):
            if not self.visited[i] and self.hasCycle(i):
                return False
        return True

    def hasCycle(self, i):
        # base
        # node is in cycle
        if self.path[i]:
            return True
        if self.visited[i]:
            return False

        # logic
        self.path[i] = True
        # get edges of curr node
        children = None
        if i in self.hMap:
            children = self.hMap[i]
        if children is not None:
            for child in children:
                # recurse
                if self.hasCycle(child):
                    return True
        # backtrack
        self.path[i] = False
        self.visited[i] = True
        return False
