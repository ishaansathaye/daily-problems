from typing import List
import deque


class Solution:
    def hasPath(self, maze: List[List[int]],
                start: List[int], destination: List[int]) -> bool:
        '''BFS'''
        if start[0] == destination[0] and start[1] == destination[1]:
            return True
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # U, D, L, R
        m = len(maze)
        n = len(maze[0])

        q = deque()
        q.append(start)
        maze[start[0]][start[1]] = 2  # marked visited (not a wall)
        while len(q) != 0:
            curr = q.pop()
            # if this is destination:
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True
            for d in dirs:
                r = curr[0]
                c = curr[1]
                # move in dir until wall
                # till in bounds and not into a wall
                while (r >= 0 and r < m and c >= 0
                       and c < n and maze[r][c] != 1):
                    r += d[0]
                    c += d[1]
                # 1 stepback
                r -= d[0]
                c -= d[1]
                # put baby inside q
                if maze[r][c] != 2:
                    q.append((r, c))
                    maze[r][c] = 2
        return False

    def _hasPath(self, maze: List[List[int]],
                 start: List[int], destination: List[int]) -> bool:
        '''DFS'''
        if start[0] == destination[0] and start[1] == destination[1]:
            return True
        self.dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # U, D, L, R
        self.m = len(maze)
        self.n = len(maze[0])
        self.flag = False
        self.dfs(maze, start, destination)
        return self.flag

    def dfs(self, maze, start, destination):
        # base
        if maze[start[0]][start[1]] == 2 or self.flag:
            return
        # logic
        if start[0] == destination[0] and start[1] == destination[1]:
            self.flag = True
            return

        maze[start[0]][start[1]] = 2

        for d in self.dirs:
            r = start[0]
            c = start[1]
            while (r >= 0 and r < self.m and c >= 0
                   and c < self.n and maze[r][c] != 1):
                r += d[0]
                c += d[1]
            r -= d[0]
            c -= d[1]
            if not self.flag:
                self.dfs(maze, (r, c), destination)
