from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]  # start with btm left as tmp (4, 0)
                # replace in clockwise manner
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

    def _rotate(self, matrix: List[List[int]]) -> None:
        '''
        Using transpose and reverse technique
        '''
        # tranpose (flip over diagonal)
        n = len(matrix)
        for i in range(n):
            # i+1 b/c not going over diagonal
            # achieve same with just i but more operations
            for j in range(i+1, n):
                # swapping elements
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse from left and right
        for i in range(n):
            # just want half of the columns of matrix
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]


if __name__ == "__main__":
    s = Solution()
    m = [
        [1, 2],
        [3, 4]
    ]
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s._rotate(m)


'''
[1 2 3]
[4 5 6]
[7 8 9]

00 01 02
10 11 12
20 21 22

00 -> 02 (i,j) -> (j, 3 - 1 - i = 0)
02 -> 22 (j, 3 - 1 - 0) -> (3 - 1 - i = 0, 3 - 1 - j = 0)
22 -> 20 (3 - 1 - i = 0, 3 - 1 - j = 0) -> (3 - 1 - j, i)
20 -> 00 (3 - 1 - j, i) -> (i, j)

3 x 3
n = 3
3 // 2 = 1
1 + 3 % 2 = 1 + 1 = 2
i = (0, 2) -> 0, 1
j = (0, 1) -> 0

n = 5
5 // 2 = 2
5 % 2 = 1
2 + 1 = 3
i = (0, 3) -> 0, 1, 2
j = (0, 2) -> 0, 1

1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

i = 0, j = 0
21 2 3 4 1
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
25 22 23 24 5

i = 0, j = 0
tmp = [5 - 1 - 0][0] -> [4][0]
i = 0, j = 1
tmp = 5 - 1 - 1 = 3 -> [3][0]
tmp = 16
(each inner loop results starting with bottom left, then 1 above bottom left)

i = 1, j = 0
tmp = 5 - 1 - 0 = 4 -> [4][1]
i = 1, j = 1
tmp = [5-1-1][1] -> [3][1]
(after 1 iteration of i -> results in small square matrix being selected as tmps)

i = 2, j = 0
tmp = [5 - 1 - 0][2] -> [4][2]
i = 2, j = 1
tmp = [5 - 1 - 1][2] -> [3][2] (inner part of matrix)

'''
