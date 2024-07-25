from typing import List


class Solution:
    dirs = None
    m = None
    n = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                # start at first letter
                if self.backtrack(board, i, j, word, 0):
                    return True
        return False

    # r and c are the current place in board, idx is palce in word
    def backtrack(self, board, r, c, word, idx):
        # base
        # if all letters are finished
        if idx == len(word):
            return True
        # bounds check
        if r < 0 or c < 0 or r == self.m or c == self.n:
            return False
        # logic
        # if current is next letter
        if board[r][c] == word[idx]:
            # action
            board[r][c] = '#'
            # recurse
            for d in self.dirs:
                nr = d[0] + r
                nc = d[1] + c
                # recurse
                if self.backtrack(board, nr, nc, word, idx+1):
                    return True
            # backtrack if not found next path
            board[r][c] = word[idx]
        return False
