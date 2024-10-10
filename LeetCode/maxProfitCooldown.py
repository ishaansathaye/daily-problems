from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        '''Time Limit Exceeded -> Exponential'''
        return self.helper(prices, 0, -1)

    def helper(self, prices, idx, prevBuy):
        # serves as state and prev value
        # prevBuy = 2
        # prevBuy = -1 (not bought it)
        # base
        if idx >= len(prices):
            return 0
        # logic
        if prevBuy == -1:
            # buy state
            # no buy
            case1 = self.helper(prices, idx+1, -1)
            # buy
            case2 = self.helper(prices, idx+1, prices[idx])
            return max(case1, case2)
        else:
            # sell state
            # no sell
            case3 = self.helper(prices, idx+1, prevBuy)
            # sell
            # + profit from rest of array
            case4 = prices[idx] - prevBuy + self.helper(prices, idx+2, -1)
            return max(case3, case4)

    def maxProfit2(self, prices: List[int]) -> int:
        '''Memoization'''
        self.memo = [[-1 for _ in range(2)] for _ in range(len(prices))]
        return self.helper(prices, 0, 0)

    def helper2(self, prices, idx, flag):
        # base
        if idx >= len(prices):
            return 0
        if self.memo[idx][flag] != -1:
            return self.memo[idx][flag]

        # logic
        if flag == 0:
            # buy state
            # no buy
            case1 = self.helper(prices, idx+1, 0)
            # buy
            case2 = -prices[idx] + self.helper(prices, idx+1, 1)
            res = max(case1, case2)
            self.memo[idx][0] = res
            return res
        else:
            # sell state
            # no sell
            case3 = self.helper(prices, idx+1, 1)
            # sell
            # + profit from rest of array
            case4 = prices[idx] + self.helper(prices, idx+2, 0)
            res = max(case3, case4)
            self.memo[idx][1] = res
            return res

    def _maxProfit(self, prices: List[int]) -> int:
        '''Tabulation'''
        if len(prices) < 2:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[1][0] = max(-prices[0], -prices[1])
        dp[1][1] = max(0, prices[1] - prices[0])
        for i in range(2, len(prices)):
            # max(not buy, buy+prevSell)
            dp[i][0] = max(dp[i-1][0], -prices[i] + dp[i-2][1])
            # max(prevSell, curr + prevBuy)
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])

        return dp[len(prices)-1][1]  # sell state

    def maxProfit(self, prices: List[int]) -> int:
        '''Tabulation: O(1) Space'''
        if len(prices) < 2:
            return 0
        # currBuy, prevSell, currSell
        currBuy = max(-prices[0], -prices[1])
        prevSell = 0
        currSell = max(0, prices[1] - prices[0])
        for i in range(2, len(prices)):
            temp = currSell
            currBuy = max(currBuy, -prices[i] + prevSell)
            currSell = max(currSell, prices[i] + currBuy)
            prevSell = temp

        return currSell
