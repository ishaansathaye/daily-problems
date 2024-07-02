from typing import List


def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    m = len(mat)  # rows
    n = len(mat[0])  # cols
    result = [0 for i in range(m*n)]
    r = 0
    c = 0
    idx = 0  # idx of result arr
    flag = True
    while idx < m*n:
        result[idx] = mat[r][c]  # put element in arr
        idx += 1
        if flag:
            # if exceeding col
            if c == n - 1:
                r += 1  # go to next row and start downward
                flag = False
            # if going to exceed upper row
            elif r == 0:
                c += 1  # go to next col and start downward
                flag = False
            else:
                # move downward
                r -= 1
                c += 1
        else:
            # if going to exceed last row
            if r == m - 1:
                c += 1
                flag = True
            # if going to exceed first col
            elif c == 0:
                r += 1
                flag = True
            else:
                # move upward
                r += 1
                c -= 1
    return result


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert findDiagonalOrder(mat) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
