from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''O(n!)'''
        result = []
        grid = [[False for _ in range(n)] for _ in range(n)]
        # can go either row by row or col by col
        self.backtrack(grid, 0, result)
        return result

    def backtrack(self, grid, r, result):
        # base
        # reached end of grid
        if r == len(grid):  # all queens are placed
            li = []  # Space: O(n)
            # go through each row of grid to make string
            for i in range(len(grid)):  # string for curr row
                sb = ""
                for j in range(len(grid)):  # Space: O(n)
                    if grid[i][j]:
                        sb += "Q"
                    else:
                        sb += "."
                li.append(sb)
            result.append(li)
            return
        # logic
        # when we are on particular row
        for c in range(len(grid)):
            # iterating through cols
            if self.isSafe(grid, r, c):
                # action
                grid[r][c] = True
                # recurse
                self.backtrack(grid, r+1, result)
                # backtrack
                grid[r][c] = False

    def isSafe(self, grid, r, c):
        # col check (go through rows)
        for i in range(0, r):
            if grid[i][c]:
                return False

        # only worried about diags above (since queens above only put)
        # diag up right
        i = r
        j = c
        while i >= 0 and j < len(grid):  # borders check
            if grid[i][j]:  # found queen
                return False
            i -= 1
            j += 1
        # diag up left
        i = r
        j = c
        while i >= 0 and j >= 0:  # borders check
            if grid[i][j]:  # found queen
                return False
            i -= 1
            j -= 1
        return True
