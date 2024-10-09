from typing import List


class Solution:
    def _maxProfit(self, prices: List[int]) -> int:
        '''Brute: O(n^2) -> Time Limit Exceeded'''
        n = len(prices)
        maxProfit = self.singleTransaction(prices, 0, n-1)
        for i in range(1, n-1):
            first = self.singleTransaction(prices, 0, i)  # O(n)
            second = self.singleTransaction(prices, i+1, n-1)  # O(n)
            maxProfit = max(maxProfit, first+second)
        return maxProfit

    def singleTransaction(self, prices, left, right):
        maxProfit = 0
        minVal = prices[left]
        for i in range(left, right+1):
            minVal = min(prices[i], minVal)
            maxProfit = max(maxProfit, prices[i]-minVal)
        return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        '''Optimized - O(n)'''
        buy1 = prices[0]
        sell1 = 0
        buy2 = prices[0]
        sell2 = 0
        n = len(prices)
        for i in range(1, n):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i]-buy1)
            # buy 2 incoroporates profit of earlier
            # transaction (profit of single transaction)
            buy2 = min(buy2, prices[i]-sell1)
            # sell 2 gets the final profit
            sell2 = max(sell2, prices[i]-buy2)
        return sell2
