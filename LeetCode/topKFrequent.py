import heapq
from collections import defaultdict
from typing import List


class Solution:
    def _topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''O(nlogk)'''
        hMap = defaultdict(int)
        for num in nums:
            hMap[num] += 1

        pq = []
        for key in hMap.keys():  # O(nlogk)
            heapq.heappush(pq, (hMap[key], key))
            if len(pq) > k:
                heapq.heappop(pq)

        res = [0]*k
        i = 0
        while len(pq) != 0:
            res[i] = heapq.heappop(pq)[1]
            i += 1
        return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''O(n) - Bucket Sort'''
        hMap = defaultdict(int)
        for num in nums:
            hMap[num] += 1

        fMap = defaultdict(list)
        minVal = 2**31
        maxVal = -2**31
        for key in hMap.keys():
            val = hMap[key]
            maxVal = max(val, maxVal)
            minVal = min(val, minVal)
            fMap[val].append(key)

        res = []
        i = 0
        for j in range(maxVal, minVal-1, -1):
            li = fMap[j]
            for m in range(len(li)):
                if i < k:
                    res.append(li[m])
                    i += 1
        return res
