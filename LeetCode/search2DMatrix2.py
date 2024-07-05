from typing import List


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = n-1
    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            # target is greater so reject curr row and move down
            i += 1
        else:
            # target is smaller so move in curr row by inside 1 col
            j -= 1
    return False
