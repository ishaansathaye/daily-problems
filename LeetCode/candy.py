from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''Option #2 - 2 Pass Solution'''
        n = len(ratings)
        res = [1 for _ in range(n)]
        # left pass
        for i in range(1, n):
            # greater than left neighbor
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        # right pass
        sumCandies = res[n-1]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # ith person gets max between current or
                # comparing with right+1
                res[i] = max(res[i], res[i+1]+1)
            sumCandies += res[i]
        return sumCandies

    def _candy(self, ratings: List[int]) -> int:
        '''Slope Solution'''
        pass
