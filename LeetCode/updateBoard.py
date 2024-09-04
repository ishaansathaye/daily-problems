from typing import List
import deque


class Solution:
    def updateBoard(self, board: List[List[str]],
                    click: List[int]) -> List[List[str]]:
        '''BFS'''
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
        q = deque()
        self.m = len(board)
        self.n = len(board[0])
        q.append(click[0])
        q.append(click[1])
        board[click[0]][click[1]] = 'B'

        while len(q) != 0:
            cr = q.popleft()
            cc = q.popleft()
            count = self.countMines(board, cr, cc, dirs)
            if count == 0:
                for d in dirs:
                    nr = d[0] + cr
                    nc = d[1] + cc
                    # bounds check and not visited
                    if (nr >= 0 and nr < self.m and nc >= 0
                            and nc < self.n and board[nr][nc] == 'E'):
                        q.append(nr)
                        q.append(nc)
                        board[nr][nc] = 'B'
            else:
                board[cr][cc] = str(count)

        return board

    def countMines(self, board, i, j, dirs):
        res = 0
        for d in dirs:
            nr = d[0] + i
            nc = d[1] + j
            if (nr >= 0 and nr < self.m and nc >= 0
                    and nc < self.n and board[nr][nc] == 'M'):
                res += 1
        return res

    def _updateBoard(self, board: List[List[str]],
                     click: List[int]) -> List[List[str]]:
        '''DFS'''
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.m = len(board)
        self.n = len(board[0])
        self.dfs(board, click[0], click[1], dirs)

        return board

    def dfs(self, board, i, j, dirs):
        # base
        if i < 0 or j < 0 or i == self.m or j == self.n or board[i][j] == 'B':
            return
        # logic
        board[i][j] = 'B'
        count = self.countMines(board, i, j, dirs)
        if count == 0:
            for d in dirs:
                nr = d[0] + i
                nc = d[1] + j
                self.dfs(board, nr, nc, dirs)
        else:
            board[i][j] = str(count)
