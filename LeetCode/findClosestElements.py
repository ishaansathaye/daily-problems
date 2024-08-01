from typing import List
from heapq import heappush, heappop


class Solution:
    def _findClosestElements(self, arr: List[int],
                             k: int, x: int) -> List[int]:
        '''Heap Solution'''
        # can also do case where first element in greater than x so no pq
        # null check
        pq = []  # max heap, dist_b - dist_a and b - a

        for i in range(len(arr)):
            dist = abs(arr[i]-x)
            heappush(pq, (-dist, -arr[i]))
            if len(pq) > k:
                heappop(pq)

        result = []
        while len(pq) != 0:
            result.append(-1*heappop(pq)[1])

        return sorted(result)

    def __findClosestElements(self, arr: List[int],
                              k: int, x: int) -> List[int]:
        '''Two Pointers -> O(n-k)'''
        n = len(arr)
        low = 0
        high = n-1

        while high-low >= k:  # when range is k then stop
            distL = abs(arr[low] - x)
            distH = abs(arr[high] - x)

            if distL > distH:
                low += 1
            else:
                high -= 1

        result = []
        for i in range(low, high+1):
            result.append(arr[i])
        return result

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''Binary Search for Start of Range'''
        n = len(arr)
        low = 0
        high = n-k
        while low < high:
            mid = low + (high - low) // 2
            # no absolute vals -> duplicate val case does not work
            # checking if starting range is good
            distS = x - arr[mid]
            distE = arr[mid+k] - x  # one extra (for the equal distance case)
            # starting greater then increase starting
            if distS > distE:
                low = mid+1
            else:
                high = mid

        result = []
        for i in range(low, low+k):
            result.append(arr[i])
        return result
