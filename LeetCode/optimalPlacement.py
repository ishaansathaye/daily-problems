from collections import deque


class Solution:
    def optimalPlacement(self, h: int, w: int, n: int) -> int:
        '''Find min distance for all buildings'''
        self.H = h
        self.W = w
        grid = [[-1 for _ in range(w)] for _ in range(h)]
        self.minVal = 2**31
        self.backtrack(grid, 0, n)
        return self.minVal

    def bfs(self, grid):
        visited = [[False for _ in range(self.W)] for _ in range(self.H)]
        q = deque()
        for i in range(self.H):
            for j in range(self.W):
                if grid[i][j] == 0:  # building
                    q.append((i, j))
                    visited[i][j] = True
        dist = 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while len(q) != 0:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                for d in dirs:
                    nr = curr[0] + d[0]
                    nc = curr[1] + d[1]
                    # bounds check
                    if (nr >= 0 and nc >= 0 and nr < self.H
                            and nc < self.W and not visited[nr][nc]):
                        q.append((nr, nc))
                        visited[nr][nc] = True
            dist += 1
        self.minVal = min(self.minVal, dist-1)

    def backtrack(self, grid, idx, n):
        # base
        # when all buildings are placed
        if n == 0:
            # bfs for the min distance
            self.bfs(grid)
            return

        # logic

        # 2D Approach:
        # if c == self.W:
        #     r = r+1
        #     c = 0
        # for i in range(r, self.H):
        #     for j in range(c, self.W):
        #         # action
        #         grid[i][j] = 0
        #         # recurse
        #         self.backtrack(grid, i, j+1, n-1)
        #         # backtrack

        # 1D Approach better:
        for i in range(idx, self.H*self.W):
            # action
            r = i//self.W
            c = i % self.W
            grid[r][c] = 0
            # recurse
            self.backtrack(grid, i+1, n-1)
            # backtrack
            grid[r][c] = -1


if __name__ == "__main__":
    s = Solution()
    res = s.optimalPlacement(5, 4, 3)
    print(res)
