from typing import List


class Solution:
    def __init__(self):
        self.dp = None
        self.m = None
        self.n = None

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''Optimized BFS Approach'''
        if mat is None:
            return
        q = []  # of type integer
        m = len(mat)
        n = len(mat[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = -1  # can also be an offset but -1 better
                else:
                    q.append((i, j))

        dist = 0
        while len(q) != 0:
            size = len(q)  # need to keep size since have dist as level
            for i in range(size):
                curr = q.pop(0)
                for d in dirs:
                    nr = d[0] + curr[0]
                    nc = d[1] + curr[1]
                    if (nr >= 0 and nc >= 0 and nr < m
                            and nc < n and mat[nr][nc]) == -1:
                        # put val into q since prevents repeatability
                        q.append((nr, nc))
                        mat[nr][nc] = dist + 1  # setting it to be the dist
                        # can also be this (using parent's distance)
                        # using the curr node's distance + 1
                        # mat[nr][nc] = mat[curr[0]][curr[1]] + 1
            dist += 1
        return mat

    def _updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''DFS with DP (eliminating some DFS calls)'''
        if mat is None:
            return
        self.m = len(mat)
        self.n = len(mat[0])
        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == 1:
                    mat[i][j] = -1

        self.dp = [[0 for j in range(self.n)] for i in range(self.m)]
        print(self.dp)
        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == -1:
                    self.dp[i][j] = self.dfs(mat, i, j)

        return self.dp

    def dfs(self, mat, i, j):
        # base is finding the nearest 0
        if i < self.m-1 and mat[i+1][j] == 0:  # bottom
            return 1
        if i > 0 and mat[i-1][j] == 0:  # up
            return 1
        if j < self.n-1 and mat[i][j+1] == 0:  # right
            return 1
        if j > 0 and mat[i][j-1] == 0:  # left
            return 1

        # logic
        top = 2**31
        bot = 2**31
        left = 2**31
        right = 2**31
        # without dp need to do dfs on all 4 adjacent
        # top
        if i > 0 and self.dp[i-1][j] != 0:  # already have the distance
            top = self.dp[i-1][j]
        # left
        if j > 0 and self.dp[i][j-1] != 0:  # already have the distance
            left = self.dp[i][j-1]
        # bottom
        if i < (self.m - 1):
            if self.dp[i+1][j] == 0:
                self.dp[i+1][j] = self.dfs(mat, i+1, j)  # recurse on bottom 0
            bot = self.dp[i+1][j]
        # right
        if j < (self.n - 1):
            if self.dp[i][j+1] == 0:
                self.dp[i][j+1] = self.dfs(mat, i, j+1)
            right = self.dp[i][j+1]

        return min(right, top, bot, left) + 1  # pick the min between all
