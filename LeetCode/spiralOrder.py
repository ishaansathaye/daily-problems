from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    m = len(matrix)  # rows
    n = len(matrix[0])  # cols
    result = []
    left = 0
    right = n - 1
    top = 0
    bottom = m - 1
    while (top <= bottom and left <= right):
        # moving from left to right
        for j in range(left, right+1):  # even if crossed loop does not run
            result.append(matrix[top][j])
        top += 1
        # recheck the while base conditions for bottom 2
        # moving from top to bottom
        for i in range(top, bottom+1):  # even if crossed for loop does not run
            result.append(matrix[i][right])
        right -= 1
        # moving from right to left
        if top <= bottom:
            for k in range(right, left-1, -1):  # need to check base cond for top and bottom
                result.append(matrix[bottom][k])
            bottom -= 1  # does not matter where placed either outside or inside if statement
        # moving from bottom to up
        if left <= right:
            for l in range(bottom, top-1, -1):  # need to check based cond for left and right
                result.append(matrix[l][left])
            left += 1  # does not matter where placed
    return result


# without checks for bottom 2 cases this fails:
# 6 is printed twice since top has crossed bottom
m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
assert spiralOrder(m) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
