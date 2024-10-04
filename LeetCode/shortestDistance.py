from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str],
                         word1: str, word2: str) -> int:
        minDist = 2**31
        p1 = -1
        p2 = -1
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
            if wordsDict[i] == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                minDist = min(minDist, abs(p1-p2))
        return minDist
