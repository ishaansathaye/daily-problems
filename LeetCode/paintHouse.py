def minCost(self, costs: List[List[int]]) -> int:
    costsR = helper(costs, 0, 0)
    costsB = helper(costs, 0, 1)
    costsG = helper(costs, 0, 2)
    return min(costsR, costsB, costsG)

def helper(costs, idx, c): # costs, what home we are on, and what color
    # base
    if idx == len(costs): # finished withj all the houses (at the end)
        return 0
    # logic
    if c == 0: # red color in current row
        # cost of red in current house
        return costs[idx][0] + 
        min(
            # we do idx+1 b/c moving to the next house
            helper(costs, idx+1, 1). # coloring blue
            helper(costs, idx+1, 2) # coloring green
        )
    if c == 1: # color is blue
        return costs[idx][1] + min(helper(costs, idx+1, 0), helper(costs, idx+1, 2))
    if c == 2:
        return costs[idx][2] + min(helper(costs, idx+1, 0), helper(costs, idx+1, 1))

# DP approach with 2D matrix;
def minCost(self, costs: List[List[int]]) -> int:
    n = len(costs)
    # int [][] dp = new int [n][3]
    dp = [[]]
    dp[n-1][0] = costs[n-1][0] # bottom rows
    dp[n-1][1] = costs[n-1][1]
    dp[n-1][2] = costs[n-1][2]
    for i in range(n-2, 0, -1): # starting from the above bottom and stopping when == 0
        dp[i][0] = costs[i][0] + min(dp[i+1][1], dp[i+1][2]) # value in costs array + min(costs not in same col)
        dp[i][1] = costs[i][1] + min(dp[i+1][0], dp[i+1][2]) # 
        dp[i][2] = costs[i][2] + min(dp[i+1][0], dp[i+1][1])
    return min(dp[0]) # minimum of first row is the answer

# DP approach with 1D matrix;
def minCost(self, costs: List[List[int]]) -> int:
    n = len(costs)
    # int [][] dp = new int [n][3]
    dp = [[]]
    reR = costs[n-1][0] # bottom rows
    reB = costs[n-1][1]
    reG = costs[n-1][2]
    for i in range(n-2, 0, -1): # starting from the above bottom and stopping when == 0
        tempR = reR # temp variable to store before overwriting
        reR = costs[i][0] + min(reB, reG) # value in costs array + min(costs not in same col)
        tempB = reB
        reB = costs[i][1] + min(tempR, reG)  
        reG = costs[i][2] + min(tempR, tempB)
    return min(reR, reB, reG)













