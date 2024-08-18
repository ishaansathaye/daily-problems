from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        hSet = set(days)
        maxDay = days[n-1]
        ways = [1, 7, 30]
        dp = [0 for i in range(maxDay+1)]
        # dp[0] = costs[0] # need to take account for days not start with 1
        for i in range(1, maxDay+1):
            if i in hSet:
                for j in range(len(ways)):
                    # if days < 0 then just use cost
                    if i-ways[j] < 0:
                        currCost = costs[j]
                    else:
                        # no need for this case
                        # if i == 1:
                        #     currCost = dp[i-1]
                        # else:
                        #     currCost = dp[i-ways[j]] + costs[j]
                        currCost = dp[i-ways[j]] + costs[j]

                    # instead just set dp[i] to massive value at beginning
                    if j == 0:
                        dp[i] = currCost
                    else:
                        dp[i] = min(dp[i], currCost)
            else:
                # not in set then just use prev
                dp[i] = dp[i-1]
        print(dp)
        return dp[len(dp)-1]
