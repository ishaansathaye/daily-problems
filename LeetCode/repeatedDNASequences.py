from typing import List


class Solution:
    def _findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        allStrings = set()
        res = set()
        for i in range(0, n-9):
            subStr = s[i:i+10]
            if subStr in allStrings:
                res.add(subStr)
            allStrings.add(subStr)
        return list(res)

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        hMap = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        if n < 10:
            return []

        allStrings = set()  # of longs (rolling hashes)
        res = set()
        hashV = 0
        kl = 4**9
        for i in range(0, n):
            # outgoing element
            # going to the end of the viable string
            if i >= 10:
                out = s[i-10]
                # reducing the contribution of out char
                hashV = hashV - (kl*hMap[out])

            # incoming element
            incoming = s[i]
            hashV = hashV*4+hMap[incoming]
            if hashV in allStrings:
                # since we are standing at the end
                # start at i-9 and end at i+1
                res.add(s[i-9:i+1])
            allStrings.add(hashV)

        return list(res)
