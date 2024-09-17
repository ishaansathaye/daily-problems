from sortedcontainers import SortedDict
from typing import List
import defaultdict


class Solution:
    def _assignBikes(self, workers: List[List[int]],
                     bikes: List[List[int]]) -> List[int]:
        '''Slow Solution since Using TreeMap (sorted keys)'''
        n = len(bikes)
        m = len(workers)
        # TreeMap:
        tMap = SortedDict()
        # can also use heap to go through smallest distances
        for i in range(n):
            for j in range(m):
                b = bikes[i]
                w = workers[j]
                dist = self.calcDist(w, b)
                if dist not in tMap:
                    tMap[dist] = []
                # storing ith bike and jth worker in map
                tMap[dist].append((i, j))

        occupied = [False]*n
        assigned = [False]*m
        res = [-1]*m
        count = 0
        for d in tMap.keys():
            li = tMap[d]
            for wb in li:
                b = wb[0]
                w = wb[1]
                if not occupied[b] and not assigned[w]:
                    occupied[b] = True
                    assigned[w] = True
                    res[w] = b
                    count += 1
                    if count == m:
                        break
        return res

    def assignBikes(self, workers: List[List[int]],
                    bikes: List[List[int]]) -> List[int]:
        '''Bucket Sort Sol'''
        n = len(bikes)
        m = len(workers)
        tMap = defaultdict(list)
        minD = 2000
        maxD = 0
        for i in range(n):
            for j in range(m):
                b = bikes[i]
                w = workers[j]
                dist = self.calcDist(w, b)
                if dist not in tMap:
                    tMap[dist] = []
                # storing ith bike and jth worker in map
                tMap[dist].append((i, j))
                minD = min(minD, dist)
                maxD = max(maxD, dist)

        occupied = [False]*n
        assigned = [False]*m
        res = [0]*m
        count = 0
        for d in range(minD, maxD+1):
            li = tMap[d]
            if li is None:
                continue
            for wb in li:
                b = wb[0]
                w = wb[1]
                if not occupied[b] and not assigned[w]:
                    occupied[b] = True
                    assigned[w] = True
                    res[w] = b
                    count += 1
                    if count == m:
                        break
        return res

    def calcDist(self, w, b):
        return abs(w[0] - b[0]) + abs(w[1] - b[1])
