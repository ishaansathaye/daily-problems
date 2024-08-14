class Solution:
    def _uniquePaths(self, m: int, n: int) -> int:
        '''Brute Force'''
        return self.helper(0, 0, m, n)

    def _helper(self, i, j, m, n):
        # base
        if i == m or j == n:
            return 0
        if i == m-1 and j == n-1:
            # 1 path
            return 1

        # logic
        right = self.helper(i, j+1, m, n)
        bottom = self.helper(i+1, j, m, n)
        return right + bottom

    def uniquePaths1(self, m: int, n: int) -> int:
        '''Top-Down DP'''
        self.memo = [[0 for _ in range(n)] for _ in range(m)]
        # put 1 in the finish
        self.memo[m-1][n-1] = 1
        return self.helper(0, 0, m, n)

    def helper(self, i, j, m, n):
        # base
        if i == m or j == n:
            # out of bounds
            return 0
        if self.memo[i][j] != 0:
            return self.memo[i][j]

        # logic
        right = self.helper(i, j+1, m, n)
        bottom = self.helper(i+1, j, m, n)
        self.memo[i][j] = right+bottom
        return self.memo[i][j]

    def uniquePaths2(self, m: int, n: int) -> int:
        '''Bottom-Up DP'''
        # extra row and col at bottom and right with 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

    def uniquePaths(self, m: int, n: int) -> int:
        '''Bottom-Up DP with O(n) Space'''
        dp = [0 for _ in range(n)]
        dp[n-1] = 1
        for i in range(m-1, -1, -1):
            # n - 2 since col is just 1s so starting with 1 less than last col
            for j in range(n-2, -1, -1):
                dp[j] = dp[j] + dp[j+1]
        return dp[0]
