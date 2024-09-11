class Solution:
    def _superEggDrop(self, k: int, n: int) -> int:
        '''Time Limit Exceeded - O(n^2*k)'''
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
        for j in range(1, n+1):
            dp[1][j] = j  # first row is just linear

        for i in range(2, k+1):  # eggs
            for j in range(1, n+1):
                # for each cell do starting each floor
                # best case among all current floors:
                minVal = 2**31
                # Binary Search to reduce O(n) to O(logn)
                for f in range(1, j+1):
                    # 1 + worse case of no break, break
                    currAttempt = 1 + max(dp[i][j-f], dp[i-1][f-1])
                    minVal = min(minVal, currAttempt)
                dp[i][j] = minVal
        return dp[k][n]

    def __superEggDrop(self, k: int, n: int) -> int:
        '''O(n*k) for time and space'''
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        attempts = 0
        while dp[attempts][k] < n:
            attempts += 1
            for j in range(1, k+1):
                dp[attempts][j] = 1 + dp[attempts-1][j-1] + dp[attempts-1][j]
        return attempts

    def superEggDrop(self, k: int, n: int) -> int:
        '''Space Optimized - O(k)'''
        dp = [0]*(k+1)
        attempts = 0
        # max floors reachable with given amount of moves
        while dp[k] < n:
            attempts += 1
            for j in range(k, 0, -1):
                dp[j] = 1 + dp[j-1] + dp[j]
        return attempts
