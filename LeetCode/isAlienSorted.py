from typing import List
from collections import defaultdict


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hMap = defaultdict(int)
        for i in range(len(order)):
            hMap[order[i]] = i

        # taking i and i+1
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            if self.notSorted(first, second, hMap):
                return False

        return True

    def notSorted(self, first, second, hMap):
        f = len(first)
        s = len(second)
        low = 0
        if f < s:
            low = f
        else:
            low = s
        for i in range(low):
            fChar = first[i]
            sChar = second[i]
            if fChar != sChar:
                # not sorted if first is greater than second
                return hMap[fChar] > hMap[sChar]
        # if chars are equal -> is second len smaller than first
        # then not sorted
        return s < f
