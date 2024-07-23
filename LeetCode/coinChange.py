from typing import List


def coinChange(self, coins: List[int], amount: int) -> int:
    # exhaustive solution in this case is a recursive tree method
    # null case
    re = helper(coins, amount, 0)
    if re >= 9999999:
        return -1
    return re


def helper(coins, amount, idx):  # 3 things: coints, amount, and at what coin you are making decision
    # what index coin is at for decision

    # base case
    if amount == 0:  # leaf node with target reached
        return 0
    if idx == len(coins) or amount < 0:  # leaf node with non-valid path
        return 9999999  # not integer max because you do not want overflow with 1 + integer max

    # logic
    # - choose
    # idx because you can reuse coins
    case1 = 1 + helper(coins, amount-coins[idx], idx)
    # - not choose
    case2 = helper(coins, amount, idx+1)
    # take min between sub trees
    return min(case1, case2)


def dp_coinChange(self, coins: List[int], amount: int) -> int:
    m = len(coins)
    n = amount
    # int [][] dp = new int[m+1][n+1]
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for j in range(1, n+1):
        # max value can be whatever is the amount + 1 (is the infinite case)
        dp[0][j] = amount + 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            # case 1 is available
            if (j < coins[i-1]):  # till the time amount < denomination of curr coint
                # no choose case
                dp[i][j] = dp[i-1][j]
            else:
                # no choose case and choose
                # amount - denomicatiom of curr coin
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]])
    re = dp[m][n]
    if re >= amount + 1:
        return -1
    return re

# further optimize then just keep 1D array so just dp[j]
