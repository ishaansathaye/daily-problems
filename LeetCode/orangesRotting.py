from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''BFS Approach'''
        # single queue of integers (taking them out in pairs)
        q = []
        # q.add(i); q.add(j)
        # can also maintain 2 queues with row and column
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        time = 0
        if fresh == 0:  # no fresh oranges
            return 0
        while len(q) != 0:
            size = len(q)  # maintain the size
            for i in range(size):
                curr = q.pop(0)
                # go to all neighbors and check if any are fresh
                for d in dirs:
                    nr = curr[0] + d[0]
                    nc = curr[1] + d[1]
                    # bounds check and fresh check
                    if (nr >= 0 and nc >= 0 and nr < m and nc < n
                            and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        fresh -= 1  # reduce fresh count
                        grid[nr][nc] = 2  # make it rotten

            time += 1  # once level is done then only increase time

        if fresh != 0:
            return -1
        return time - 1
