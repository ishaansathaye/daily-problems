from typing import List


class Solution:
    def _hIndex(self, citations: List[int]) -> int:
        '''Linear Solution'''
        if citations is None or len(citations) == 0:
            return 0
        n = len(citations)
        for i in range(n):
            diff = n - i
            if diff <= citations[i]:
                return diff
        return 0

    def hIndex(self, citations: List[int]) -> int:
        '''Binary Search Solution'''
        n = len(citations)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            diff = n - mid
            if citations[mid] == diff:
                return diff
            elif citations[mid] > diff:
                # move left since want citation is greater
                high = mid - 1
            else:
                # move right since want to find first switch
                low = mid + 1
        # where low has landed is the solution
        return n - low
