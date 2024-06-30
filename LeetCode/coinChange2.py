# Exhaustive approach: O(2^m+n)
def change(self, amount: int, coins: List[int]) -> int:
    return helper(coins, 0, amount)

def helper(coins, idx, amount):
    # base
    if amount == 0:
        return 1
    if amount < 0 or idx == len(coins): # negative or reached the end of coins
        return 0
    # logic
    # choose
    case1 = helper(coins, idx, amount - coins[idx])

    # not choose
    case1 = helper(coins, idx+1, amount)

    return case1+case2

# DP Approach 2D:
def change(self, amount: int, coins: List[int]) -> int:
    m = len(coins)
    n = amount
    # int [][] dp = new int[m+1][n+1]
    dp = [[]]
    dp[0][0] = 1
    for i in range(0, m+1):
        dp[i][0] = 1 # first col to 1
    for i in range(1, m+1): # <= m b/c going to m
        for j in range(1, n+1): # <= n b/c going to n
            # till coin denom is greater than amount we have no choose case only
            if j < coin[i-1]: # i - 1 b/c have to start with dummy
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]] # one above + (denominations back)
    return dp[m][n]

# DP Approach 1D:
def change(self, amount: int, coins: List[int]) -> int:
    m = len(coins)
    n = amount
    dp = []
    dp[0] = 1
    for i in range(1, m+1): 
        for j in range(1, n+1):
            if j < coin[i-1]:
                dp[j] = dp[j]
            else:
                dp[j] = dp[j] + dp[j - coins[i-1]] # current + (denomincation back)
    return dp[n]

