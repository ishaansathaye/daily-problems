from typing import List
import defaultdict


class Solution:
    def __minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        '''Original Sol'''
        hMap = defaultdict(int)
        for i in range(len(tops)):
            hMap[tops[i]] += 1
            hMap[bottoms[i]] += 1

        val = -1
        for j in hMap.keys():
            if hMap[j] >= len(tops):
                val = j
        if val == -1:
            return val

        topsCount = 0
        botCount = 0
        for i in range(len(tops)):
            if tops[i] != val and bottoms[i] != val:
                return -1
            if tops[i] == val:
                if tops[i] != bottoms[i]:
                    topsCount += 1
            if bottoms[i] == val:
                if tops[i] != bottoms[i]:
                    botCount += 1
        return min(topsCount, botCount)

    def _minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        '''s30'''
        hMap = defaultdict(int)
        target = -1
        for i in range(len(tops)):
            hMap[tops[i]] += 1
            if hMap[tops[i]] >= len(tops):
                target = tops[i]

            hMap[bottoms[i]] += 1
            if hMap[bottoms[i]] >= len(tops):
                target = bottoms[i]
                break

        if target == -1:
            return -1
        tRot = 0
        bRot = 0
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return -1
            if tops[i] != target:
                tRot += 1
            if bottoms[i] != target:
                bRot += 1
        return min(tRot, bRot)

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        '''without hash map'''
        re = self.check(tops, bottoms, tops[0])
        if re != -1:
            return re
        # only have to check starting pair:
        return self.check(tops, bottoms, bottoms[0])

    def check(self, tops, bottoms, target):
        tRot = 0
        bRot = 0
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return -1
            if tops[i] != target:
                tRot += 1
            if bottoms[i] != target:
                bRot += 1
        return min(tRot, bRot)
