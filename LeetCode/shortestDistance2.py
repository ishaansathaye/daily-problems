from typing import List
from collections import defaultdict


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hMap = defaultdict(list)
        for i in range(len(wordsDict)):
            self.hMap[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        word1List = self.hMap[word1]
        word2List = self.hMap[word2]
        # Two Pointers on Sorted Lists
        p1 = 0
        p2 = 0
        minDist = 2**31
        while p1 < len(word1List) and p2 < len(word2List):
            minDist = min(minDist, abs(word1List[p1]-word2List[p2]))
            if word1List[p1] < word2List[p2]:
                p1 += 1
            else:
                p2 += 1
        return minDist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
