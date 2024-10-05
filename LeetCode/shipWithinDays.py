from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowerBound = weights[0]  # max of weights
        upperBound = 0  # sum of weights
        for w in weights:
            lowerBound = max(lowerBound, w)
            upperBound += w

        while lowerBound <= upperBound:
            mid = lowerBound + (upperBound - lowerBound) // 2
            # at this capacity how many days needed
            currDays = 1
            currWeight = 0
            for i in range(len(weights)):
                if currWeight + weights[i] > mid:
                    currDays += 1
                    currWeight = 0
                currWeight += weights[i]
            # if curr days is less then move to greater side
            if currDays <= days:
                upperBound = mid - 1
            else:
                lowerBound = mid + 1

        return lowerBound
