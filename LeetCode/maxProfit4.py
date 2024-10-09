from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [2**31]*(k+1)
        sell = [0]*(k+1)
        # buy[0] = min(buy[0], prices[0]) # still would be prices[0]
        # since infinity
        # do not need since not considering buy[0]
        for i in range(len(prices)):
            for j in range(1, k+1):
                # min between current buy and previous sell
                # same as sell1
                buy[j] = min(buy[j], prices[i] - sell[j-1])
                # max between current sell and curr price - current buy
                sell[j] = max(sell[j], prices[i] - buy[j])
        return sell[k]
