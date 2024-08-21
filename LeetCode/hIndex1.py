from typing import List


class Solution:
    def _hIndex(self, citations: List[int]) -> int:
        '''Sorting Method'''
        citations.sort()
        n = len(citations)
        for i in range(n):
            temp = n-i
            if temp <= citations[i]:
                return temp
        return 0

    def hIndex(self, citations: List[int]) -> int:
        '''Bucket Sort Method'''
        n = len(citations)
        arr = [0 for i in range(n+1)]
        for i in range(n):
            if citations[i] >= n:
                arr[n] += 1
            else:
                arr[citations[i]] += 1

        temp = 0
        for i in range(n, -1, -1):
            temp += arr[i]
            if temp >= i:
                return i
        return 0
