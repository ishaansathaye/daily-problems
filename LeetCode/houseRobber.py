# exhaustive case: O(2^n)
def rob(self, nums: List[int]) -> int:
    # null case
    return helper(nums, 0)

def helper(nums, idx) -> int:
    # base
    if idx >= len(nums):
        return 0

    # logic
    # choose
    case1 = nums[idx] + helper(nums, idx+2)
    # not choose
    case2 = 0 + helper(nums, idx+1)
    return max(case1, case2)

# DP approach 1D approach:
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    # dp = new int[n]
    dp = []
    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1]+0) # max between first 2 nums
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[n-1]

# Space optimized: O(1)
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    prev = nums[0]
    curr = max(dp[0], nums[1]+0) # max between first 2 nums
    for i in range(2, n):
        temp = curr
        curr = max(curr, prev+nums[i])
        prev = temp
    return curr

