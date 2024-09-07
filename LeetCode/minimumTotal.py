from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''Bottom Up: starting from bottom - O(n^2)'''
        n = len(triangle)
        # starting from second last row
        for i in range(n-2, -1, -1):
            # iterate on the size of the row
            # for j in range(0, len(triangle[i])):
            # or on the row since row is # of elements
            # +1 because current is the longer row
            for j in range(0, i+1):
                # compare 2 consecutive elements
                minFromBottom = min(triangle[i+1][j], triangle[i+1][j+1])
                # set at current location
                triangle[i][j] += minFromBottom
        # get only first element
        return triangle[0][0]

    def __minimumTotal(self, triangle: List[List[int]]) -> int:
        '''Bottom Up: starting from top - O(n^2)'''
        n = len(triangle)
        for i in range(1, n):
            for j in range(0, i+1):
                # at edge soem diff
                if j == 0:
                    # at beginning
                    # curr to curr + prev row element
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                elif j == i:
                    # if at the end
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                else:
                    # all other cases (compare 2 from above row)
                    triangle[i][j] = triangle[i][j] + \
                        min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[n-1])

    def _minimumTotal(self, triangle: List[List[int]]) -> int:
        '''Top Down DP: Memoization'''
        n = len(triangle)
        self.memo = [[0 for _ in range(n)] for _ in range(n)]
        # -1 means not evaluated that index
        for i in range(n):
            for j in range(i+1):
                self.memo[i][j] = -1
        # triangle, which row we are on, which col we are on
        temp = self.helper(triangle, 0, 0)
        print(self.memo)
        return temp

    def helper(self, triangle, i, j):
        # base
        if i == len(triangle):
            return 0
        if self.memo[i][j] != -1:
            # no need to recalc values if already there in memo
            return self.memo[i][j]

        # logic
        # fall to jth index
        case1 = self.helper(triangle, i+1, j)
        # fall to j+1th index
        case2 = self.helper(triangle, i+1, j+1)

        self.memo[i][j] = triangle[i][j] + min(case1, case2)
        return self.memo[i][j]
