from typing import List
import defaultdict


class Solution:
    '''Tarjon's Algorithm'''

    def criticalConnections(self, n: int,
                            connections: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.discovery = [-1 for _ in range(n)]
        self.lowest = [0 for _ in range(n)]
        self.time = 0
        self.hMap = defaultdict(list)
        self.buildGraph(connections, n)
        self.dfs(0, 0)
        return self.res

    def buildGraph(self, connections, n):
        # for i in range(0, n):
        #     hMap[i] = []
        for edge in connections:
            n1 = edge[0]
            n2 = edge[1]
            self.hMap[n1].append(n2)
            self.hMap[n2].append(n1)

    def dfs(self, v, u):
        if self.discovery[v] != -1:
            return
        self.discovery[v] = self.time
        self.lowest[v] = self.time
        self.time += 1

        for n in self.hMap[v]:
            if n == u:
                continue
            self.dfs(n, v)
            if self.lowest[n] > self.discovery[v]:
                self.res.append((n, v))
            self.lowest[v] = min(self.lowest[v], self.lowest[n])
