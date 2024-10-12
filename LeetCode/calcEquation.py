from typing import List
from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]],
                     values: List[float],
                     queries: List[List[str]]) -> List[float]:
        '''BFS'''
        graph = defaultdict(defaultdict)
        # build graph given equations
        for i in range(len(equations)):
            eq = equations[i]
            graph[eq[0]][eq[1]] = values[i]
            graph[eq[1]][eq[0]] = 1/values[i]

        # bfs on queries
        res = [-1]*len(queries)
        for i in range(len(queries)):
            numer, denom = queries[i][0], queries[i][1]
            if numer not in graph or denom not in graph:
                res[i] = -1
                continue
            elif numer == denom:
                res[i] = 1
                continue
            else:
                q = deque()
                visited = set()
                # numerator and accumulated value at that numerator
                q.append((numer, 1))
                visited.add(numer)
                while len(q) != 0:
                    curr, currValue = q.popleft()
                    if curr == denom:
                        res[i] = currValue
                        break
                    for child, value in graph[curr].items():
                        if child not in visited:
                            visited.add(child)
                            q.append((child, currValue * graph[curr][child]))
        return res

    def _calcEquation(self, equations: List[List[str]],
                      values: List[float],
                      queries: List[List[str]]) -> List[float]:
        '''DFS'''
        graph = defaultdict(defaultdict)
        # build graph given equations
        for i in range(len(equations)):
            eq = equations[i]
            graph[eq[0]][eq[1]] = values[i]
            graph[eq[1]][eq[0]] = 1/values[i]

        res = []
        for q in queries:
            numer, denom = q[0], q[1]
            if numer not in graph or denom not in graph:
                res.append(-1)
            elif numer == denom:
                res.append(1)
            else:
                visited = set()
                res.append(self.dfs(graph, 1, numer, denom, visited))
        return res

    def dfs(self, graph, total, numer, denom, visited):
        # base
        if numer == denom:
            return total
        if numer in visited:
            return -1
        # logic
        visited.add(numer)
        for child, value in graph[numer].items():
            if child not in visited:
                val = self.dfs(
                    graph, total*graph[numer][child], child, denom, visited)
                if val != -1:
                    return val
        return -1
