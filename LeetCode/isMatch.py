class Solution:
    def _isMatch(self, s: str, p: str) -> bool:
        '''SC: O(mxn)'''
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True  # dash and dash is True
        # top row handling sparately (dash)
        for j in range(1, n+1):
            if p[j-1] == "*":
                # look 2 steps back
                dp[0][j] = dp[0][j-2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                # * case
                if p[j-1] == "*":
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        # one case is available to us
                        # preceding char of p is matching curr char in s
                        # 2 steps back or above (matching subproblems)
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        # look 2 steps back (without * and prev
                        # char sub problem)
                        dp[i][j] = dp[i][j-2]
                # not * case
                else:
                    # check if characters match or any wildcard
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        # sub problem is diagonal up
                        # cancel out equal chars or dots
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        return dp[m][n]

    def isMatch(self, s: str, p: str) -> bool:
        '''SC: O(n) - 1D array'''
        m = len(s)
        n = len(p)
        dp = [False for _ in range(n+1)]
        dp[0] = True  # dash and dash is True
        # top row handling sparately (dash)
        for j in range(1, n+1):
            if p[j-1] == "*":
                # look 2 steps back
                dp[j] = dp[j-2]

        for i in range(1, m+1):
            diagUp = dp[0]
            # overwriting to False for first row since it was True for dash
            dp[0] = False
            for j in range(1, n+1):
                # * case
                # save the diagonal value
                temp = dp[j]
                if p[j-1] == "*":
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        # just above is dp[j]
                        dp[j] = dp[j-2] or dp[j]
                    else:
                        dp[j] = dp[j-2]
                # not * case
                else:
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        dp[j] = diagUp
                    else:
                        dp[j] = False
                diagUp = temp

        return dp[n]
