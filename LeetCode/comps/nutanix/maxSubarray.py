# Problem: Maximum Subarray in HackerRank
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


def maxSubArrayLC(nums):
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


print(maxSubarray([2, -1, 2, 3, 4, -5]))
