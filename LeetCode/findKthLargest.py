from typing import List
import heapq as hq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''Min Heap'''
        pq = []  # java max heap is (a,b) -> b - a; min is heap is a - b
        for i in range(len(nums)):  # O(n)
            hq.heappush(pq, nums[i])  # O(log k)
            if len(pq) > k:  # want to maintain k elements
                hq.heappop(pq)  # pop the smallest O(log k)
        return pq[0]  # peeking

    def _findKthLargest(self, nums: List[int], k: int) -> int:
        '''Max Heap: O(nlogn-k)'''
        pq = []  # b - a in java
        result = 2**31
        n = len(nums)
        for i in range(n):
            hq.heappush(pq, nums[i]*-1)
            if len(pq) > (n - k):  # want to maintain n-k eleme
                # compare between max values
                result = min(result, hq.heappop(pq)*-1)
        return result
