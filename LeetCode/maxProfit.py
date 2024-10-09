from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minVal = prices[0]
        for i in range(len(prices)):
            minVal = min(prices[i], minVal)
            maxProfit = max(maxProfit, prices[i]-minVal)
        return maxProfit
