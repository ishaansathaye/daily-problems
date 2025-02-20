from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''DFS'''
        n = len(board)  # rows
        m = len(board[0])  # cols
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # Go through borders
        # Mark O with A to keep them
        # Using DFS on their neighbors
        borders = []
        for i in range(n):
            for j in range(m):
                if ((i == 0 or j == 0 or i == n-1 or j == m-1)
                        and board[i][j] == 'O'):
                    borders.append([i, j])
        for r, c in borders:
            self.dfs(board, r, c, dirs)

        # make all the rest O -> X
        # make the A -> O
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

    def dfs(self, board, i, j, dirs):
        # base case with only O case and bounds check
        if (i < 0 or j < 0 or i == len(board) or j == len(board[0])
                or board[i][j] != 'O'):
            return

        board[i][j] = 'A'
        for d in dirs:
            nr = d[0] + i
            nc = d[1] + j
            self.dfs(board, nr, nc, dirs)

    def bfs_solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''BFS'''
        n = len(board)  # rows
        m = len(board[0])  # cols
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # Go through borders
        # Mark O with A to keep them
        # Using BFS on their neighbors
        borders = []
        for i in range(n):
            for j in range(m):
                if ((i == 0 or j == 0 or i == n-1 or j == m-1)
                        and board[i][j] == 'O'):
                    borders.append([i, j])

        q = deque()
        for r, c in borders:
            q.append((r, c))
            board[r][c] = 'A'
            while len(q) != 0:
                curr = q.popleft()
                for d in dirs:
                    nr = d[0] + curr[0]
                    nc = d[1] + curr[1]
                    if (nr >= 0 and nc >= 0 and nr < n and nc < m
                            and board[nr][nc] != 'A'):
                        q.append((nr, nc))
                        board[nr][nc] = 'A'

        # make all the rest O -> X
        # make the A -> O
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'


'''
"X","X","X","X"],
"X","O","O","X"],
"X","X","O","X"],
"X","O","X","X"]]
'''

if __name__ == "__main__":
    mat = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
           ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s = Solution()
    s.solve(mat)
    assert mat == [["X", "X", "X", "X"], ["X", "X", "X", "X"],
                   ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
