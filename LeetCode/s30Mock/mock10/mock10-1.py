from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        for i in range(1, n):
            # checking for 1st buy and 2nd sell pairs
            # where the sell is greater than the buy
            # if not then just buy and sell same day
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit

    def _maxProfit(self, prices):
        '''s30 Solution'''
        n = len(prices)
        if n == 0:
            return 0
        i = 0  # pointer
        valley = prices[0]
        peak = prices[0]
        maxProfit = 0
        # finding peak and valley
        while i < n-1:
            # go until local min is found
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            # go until local max is found
            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            maxProfit += peak - valley
        return maxProfit
