# Problem: Maximum Subarray in HackerRank
from typing import List


def maxSubarray(arr):
    # Write your code here
    arrSol = 0
    seqSol = 0
    n = len(arr)
    if n == 1:
        arrSol = arr[0]
    else:
        dp = [0 for i in arr]
        dp[0] = arr[0]
        dp[1] = max(arr[1]+dp[0], arr[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1]+arr[i], arr[i])
        arrSol = max(dp)

    seqSol = min(0, max(arr))
    for i in range(n):
        if arr[i] > 0:
            seqSol += arr[i]

    return [arrSol, seqSol]


# Problem: Maximum Subarray in LeetCode


class Solution:
    def _maxSubArray(self, nums: List[int]) -> int:
        '''DP Approach'''
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            dp = [0 for i in nums]
            dp[0] = nums[0]
            dp[1] = max(nums[1]+dp[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1]+nums[i], nums[i])
            return max(dp)

    def maxSubArray1(self, nums: List[int]) -> int:
        '''Running Sum Approach'''
        n = len(nums)
        rSum = nums[0]
        maxSum = nums[0]
        for i in range(1, n):
            rSum = max(nums[i], rSum+nums[i])
            maxSum = max(rSum, maxSum)
        return maxSum

    def maxSubArray2(self, nums: List[int]) -> int:
        '''Finding the Index of Subarray'''
        n = len(nums)
        rSum = nums[0]
        maxSum = nums[0]
        start = 1
        end = 1
        currStart = 1
        # currEnd will always be i
        for i in range(1, n):
            rSum += nums[i]
            if nums[i] > rSum:
                # if rSum changing
                rSum = nums[i]
                currStart = i
            if rSum > maxSum:
                # if maxSum is changing
                maxSum = rSum
                start = currStart
                end = i
        print(start, end)
        return maxSum
