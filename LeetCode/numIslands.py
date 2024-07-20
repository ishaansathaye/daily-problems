from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''BFS'''
        # null check
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = []  # of integers
        m = len(grid)
        n = len(grid[0])

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    result += 1
                    # bfs
                    q.append((i, j))
                    grid[i][j] = "0"  # make the first one 0
                    while len(q) != 0:
                        # no need to keep size for this one
                        curr = q.pop(0)
                        for d in dirs:
                            nr = d[0] + curr[0]
                            nc = d[1] + curr[1]
                            # bounds check
                            if (nr >= 0 and nc >= 0 and nr < m and nc < n
                                    and grid[nr][nc] == "1"):
                                q.append((nr, nc))
                                # make it 0 after finding connections
                                grid[nr][nc] = "0"
        return result

    def _numIslands(self, grid: List[List[str]]) -> int:
        '''BFS'''
        # null check
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m = len(grid)
        n = len(grid[0])

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    result += 1
                    # dfs
                    self.dfs(grid, i, j, dirs)
        return result

    def dfs(self, grid, i, j, dirs):
        # base same intuition as bounds check in bfs
        if (i < 0 or j < 0 or i == len(grid) or j == len(grid[0])
                or grid[i][j] == "0"):
            return

        # logic
        grid[i][j] = "0"  # after finding 1 make it 0
        for d in dirs:
            nr = d[0] + i
            nc = d[1] + j
            self.dfs(grid, nr, nc, dirs)
