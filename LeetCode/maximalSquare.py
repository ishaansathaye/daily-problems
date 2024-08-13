from typing import List


class Solution:
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        '''Brute Force'''
        maxA = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    length = 1  # initial length
                    flag = True
                    # bounds
                    while flag and i+length < m and j+length < n:
                        # if all are 1s in the col (going up)
                        for k in range(i+length, i-1, -1):
                            if matrix[k][j+length] == '0':
                                flag = False
                                break
                        # if all are 1s in upto left boundary
                        for k in range(j+length, j-1, -1):
                            if matrix[i+length][k] == '0':
                                flag = False
                                break
                        if flag:
                            length += 1
                    maxA = max(maxA, length)
        return maxA*maxA

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        '''DP: O(mxn) Both'''
        maxA = 0
        m = len(matrix)
        n = len(matrix[0])
        # 1 extra row and col (dummy)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    curr = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    dp[i][j] = curr
                    maxA = max(maxA, curr)
        return maxA*maxA

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''DP: TC is O(mxn) and SC is O(n)'''
        maxA = 0
        m = len(matrix)
        n = len(matrix[0])
        # 1 extra row and col (dummy)
        dp = [0 for j in range(n+1)]
        for i in range(1, m+1):
            diagUp = 0
            for j in range(1, n+1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    curr = min(dp[j], dp[j-1], diagUp) + 1
                    # j is equivalent to looking up
                    # going by row
                    dp[j] = curr
                    maxA = max(maxA, curr)
                else:
                    # need to overwrite since 1D
                    dp[j] = 0
                diagUp = temp
        return maxA*maxA


class Solution2:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        # dp = [[0]*(cols+1) for _ in range(rows+1)]
        dp = []
        for i in range(rows+1):
            row = []
            for j in range(cols + 1):
                row.append(0)
            dp.append(row)
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    # Be careful of the indexing since dp
                    # grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])

        return max_side * max_side


if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    s = Solution()
    print(s.maximalSquare(matrix))
