class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1 = text1
        s2 = text2
        m = len(s1)
        n = len(s2)
        # extra 0 in first row and col
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    # current len becomes len at prev letter
                    # or remove first letter from each
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # else current len becomes max
                    # at either prev chars for both strings
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
