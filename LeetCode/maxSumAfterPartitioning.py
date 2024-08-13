from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        '''Can also be 2D'''
        n = len(arr)
        dp = [0 for i in range(n)]
        dp[0] = arr[0]
        for i in range(n):
            currPartMax = arr[i]
            # make all the partitions (1->k)
            for j in range(1, k+1):
                # check if partitioning at the beginning:
                if i-j+1 >= 0:
                    # finding the max element with incoming
                    currPartMax = max(currPartMax, arr[i-j+1])
                    # current partition + earlier partition sum in dp
                    currSum = currPartMax*j
                    # check if earlier parition is in range
                    if i-j >= 0:
                        currSum += dp[i-j]
                    # take max of all k partitions on i
                    dp[i] = max(dp[i], currSum)
        return dp[n-1]
