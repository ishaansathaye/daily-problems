def knapsack01(n, W, profit, weight):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(0, n+1):
        for j in range(0, W+1):
            # 0 for first row/col allows for pattern checking
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                # if the item's weight is greater than current weight then
                #   use earlier's item's profit at that weight
                if (weight[i-1] > j):
                    dp[i][j] = dp[i-1][j]
                else:
                    # check between these max:
                    # - current item's profit + the profit at previous
                    #   level that is still available ([j - weight[i-1]])
                    #   - if j is 4 and weight at current is 3 then use
                    #       profit from above at 4-3=1 so d[i-1][1]
                    # - above value which is so far the max profit at that
                    #   current weight
                    dp[i][j] = max(profit[i-1] + dp[i-1][j-weight[i-1]],
                                   dp[i-1][j])
    return dp, dp[n][W]

# can optimize space for O(w) instead of O(n*w)

m, answ = knapsack01(3, 4, [2, 1, 10], [1, 2, 3])
assert answ == 12
for i in range(0, len(m)):
    print(m[i])
