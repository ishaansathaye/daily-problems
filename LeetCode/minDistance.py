class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # filling top row (dash)
        for j in range(0, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            dp[i][0] = i  # always i for dash col
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    # skip case so diag up
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
        return dp[m][n]

    def _minDistance(self, word1: str, word2: str) -> int:
        '''Space Optimized'''
        m = len(word1)
        n = len(word2)
        dp = [0 for _ in range(n+1)]
        # filling top row (dash)
        for j in range(0, n+1):
            dp[j] = j

        for i in range(1, m+1):
            diagUp = dp[0]
            dp[0] = i  # always i for dash col
            for j in range(1, n+1):
                temp = dp[j]
                if word1[i-1] == word2[j-1]:
                    # skip case so diag up
                    dp[j] = diagUp
                else:
                    dp[j] = min(dp[j], diagUp, dp[j-1])+1
                diagUp = temp
        return dp[n]
