from typing import List


def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # 0 --> 1 as 3
    # 1 --> 0 as 4
    m = len(board)
    n = len(board[0])
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0),
            (-1, 1), (-1, -1), (1, -1), (1, 1)]
    for i in range(m):
        for j in range(n):
            alives = countAlive(board, i, j, dirs)
            if board[i][j] == 1:
                # rules for alive -> dead
                if alives > 3 or alives < 2:
                    board[i][j] = 4
            else:
                # rules for dead -> alive
                if alives == 3:
                    board[i][j] = 3
    for i in range(m):
        for j in range(n):
            if board[i][j] == 3:
                board[i][j] = 1
            if board[i][j] == 4:
                board[i][j] = 0

# use directions array


def countAlive(board, r, c, dirs):
    count = 0
    for dir in dirs:
        # neighbour row index
        nr = r + dir[0]
        nc = c + dir[1]
        # bounds checking for neighbour (if in bounds and
        #   alive means 1 or 4 (state change from 1))
        if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and (
                board[nr][nc] == 1 or board[nr][nc] == 4):
            count += 1
    return count
