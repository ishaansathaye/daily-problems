from typing import List
from collections import defaultdict


class Solution:
    def ShortestWordDistance2(self, wordsDict: List[str],
                              word1: str, word2: str) -> int:
        '''ShortestWordDistance2 Original Solution'''
        hMap = defaultdict(list)
        for i in range(len(wordsDict)):
            hMap[wordsDict[i]].append(i)

        word1List = hMap[word1]
        word2List = hMap[word2]
        # Two Pointers on Sorted Lists
        p1 = 0
        p2 = 0
        minDist = 2**31
        while p1 < len(word1List) and p2 < len(word2List):
            if word1 == word2 and p1 == p2:
                p1 += 1
                continue
            minDist = min(minDist, abs(word1List[p1]-word2List[p2]))
            if word1List[p1] < word2List[p2]:
                p1 += 1
            else:
                p2 += 1
        return minDist

    def shortestWordDistance1(self, wordsDict: List[str],
                              word1: str, word2: str) -> int:
        p1 = -1
        p2 = -1
        minDist = 2**31
        if word1 == word2:
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    # if p1 < p2:
                    #     p1 = i
                    # else:
                    #     p2 = i
                    # or
                    # moving prev to curr
                    # moving curr to next
                    p1 = p2
                    p2 = i
                if p1 != -1 and p2 != -1:
                    minDist = min(minDist, abs(p1-p2))

        else:
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    p1 = i
                if wordsDict[i] == word2:
                    p2 = i
                if p1 != -1 and p2 != -1:
                    minDist = min(minDist, abs(p1-p2))
        return minDist

    def shortestWordDistance(self, wordsDict: List[str],
                             word1: str, word2: str) -> int:
        p1 = -1
        p2 = -1
        minDist = 2**31
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
            if wordsDict[i] == word2:
                # word1 equals to word2
                if p1 == i:
                    p1 = p2
                p2 = i
            if p1 != -1 and p2 != -1:
                minDist = min(minDist, abs(p1-p2))

        return minDist
