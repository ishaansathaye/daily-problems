from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inD = [0 for i in range(n)]
        for t in trust:
            inD[t[0]-1] -= 1
            inD[t[1]-1] += 1

        for i in range(n):
            if inD[i] == n-1:
                return i+1
        return -1

    # can also do hashset solution and keep count of how much trusting
    # does not appear in the first position
