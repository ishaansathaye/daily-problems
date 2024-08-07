from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''Sliding Window: Ingoing and Outgoing Chars'''
        hMap = {}  # <Character, Integer> (occurrences)
        res = []
        for i in range(len(p)):
            if p[i] not in hMap:
                hMap[p[i]] = 0
            hMap[p[i]] += 1
        print(hMap)

        matchCount = 0
        for i in range(len(s)):
            # incoming character
            # right side character
            inC = s[i]
            if inC in hMap:
                cnt = hMap[inC] - 1
                hMap[inC] = cnt
                if cnt == 0:
                    matchCount += 1

            # outgoing character
            # only want outgoing letters from len(p) onwards
            if i >= len(p):
                outC = s[i-len(p)]  # first pointer
                if outC in hMap:
                    cnt = hMap[outC] + 1
                    hMap[outC] = cnt
                    if cnt == 1:
                        matchCount -= 1

            if matchCount == len(hMap):
                res.append(i-len(p)+1)  # +1 to get index of starting

        return res
