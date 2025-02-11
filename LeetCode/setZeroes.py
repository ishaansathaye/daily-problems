from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''Original Solution: O(m*n)'''
        m = len(matrix[0])  # num of columns
        n = len(matrix)  # num of rows

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # set cols
                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = "T"
                    # set rows
                    for h in range(m):
                        if matrix[i][h] != 0:
                            matrix[i][h] = "T"
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "T":
                    matrix[i][j] = 0
            # print(matrix[i])


'''
1. found 0 -> set rows and cols of it to -1
- if in row and col is 0 then leave
2. Replace all -1 with 0 at the end (2nd pass)
'''

if __name__ == "__main__":
    s = Solution()
    s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
