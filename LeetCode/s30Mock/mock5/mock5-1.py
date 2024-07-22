from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''IS Sol'''
        for i in range(9):
            rMap = set()
            cMap = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in rMap:
                        rMap.add(board[i][j])
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in cMap:
                        cMap.add(board[j][i])
                    else:
                        return False

        corners = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
                   (3, 6), (6, 0), (6, 3), (6, 6)]
        dirs = [(0, 0), (0, 1), (0, 2),
                (1, 0), (1, 1), (1, 2),
                (2, 0), (2, 1), (2, 2)]
        for c in corners:
            if self.validate(board, c, dirs) is False:
                return False

        return True

    def validate(self, board, corner, dirs):
        subMap = set()
        for d in dirs:
            elem = board[corner[0]+d[0]][corner[1]+d[1]]
            if elem != ".":
                if elem not in subMap:
                    subMap.add(elem)
                else:
                    return False

    def _isValidSudoku(self, board: List[List[str]]) -> bool:
        '''s30 Sol'''

        # row
        for i in range(9):
            b = [0 for k in range(9)]
            for j in range(9):
                if board[i][j] != ".":
                    if b[ord(board[i][j]) - ord("1")]:
                        # if already in array return False
                        return False
                    b[ord(board[i][j]) - ord("1")] = True

        # col
        for i in range(9):
            b = [0 for k in range(9)]
            for j in range(9):
                if board[j][i] != ".":
                    if b[ord(board[j][i]) - ord("1")]:
                        # if already in array return False
                        return False
                    b[ord(board[j][i]) - ord("1")] = True

        # 3x3 grid
        for block in range(9):
            b = [0 for k in range(9)]
            for i in range(((block//3)*3), ((block//3)*3)+3):
                for j in range(((block % 3)*3), ((block % 3)*3)+3):
                    if board[i][j] != ".":
                        if b[ord(board[i][j]) - ord("1")]:
                            # if already in array return False
                            return False
                        b[ord(board[i][j]) - ord("1")] = True

        return True
