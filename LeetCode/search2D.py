from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1  # last index of the matrix
        while low <= high:

            mid = low + (high - low) // 2

            r = mid // n

            c = mid % n  # how many indexes away or the remainder
            # (steps away from the beginning of the row)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        # use this if low < high in while loop
        # r = low/n
        # c = low%n
        # if(matrix[r][c] == target):
        #     return True
        return False
    
# fill a matrix with all 0s
def fillMatrix(m: int, n: int) -> List[List[int]]:
    matrix = []
    for i in range(m):
        matrix.append([0] * n)
    return
