class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""  # O(s) space
        sMap = {}
        for char in s:
            if char not in sMap:
                sMap[char] = 0
            sMap[char] += 1

        for char in order:
            if char in sMap:
                for i in range(sMap[char]):
                    res += char
                del sMap[char]

        for c in sMap.keys():
            for i in range(sMap[c]):
                res += c

        return res
