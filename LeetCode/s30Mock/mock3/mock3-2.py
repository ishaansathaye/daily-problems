from typing import List


def generate(numRows: int) -> List[List[int]]:  # O(n^2) is optimal
    res = []
    for i in range(0, numRows):
        row = [1]
        for j in range(1, i):
            if j != 0 and j != i:
                row.append(res[i-1][j-1]+res[i-1][j])
        if i > 0:
            row.append(1)
        res.append(row)
    return res


print(generate(5))
