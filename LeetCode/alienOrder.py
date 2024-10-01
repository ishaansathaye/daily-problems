from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:  # E
        res = []
        # can have multiple conclusions for dependencies
        # so take a set of characters
        hMap = defaultdict(set)
        inDegrees = [0]*26
        self.buildGraph(words, hMap, inDegrees)
        q = deque()
        count = 0
        print(hMap)
        for key in hMap.keys():
            if inDegrees[ord(key) - ord('a')] == 0:
                q.append(key)
                res.append(key)
                count += 1
        if len(q) == 0:
            return ""
        while len(q) != 0:  # O(V+E)
            parent = q.popleft()
            for child in hMap[parent]:
                inDegrees[ord(child) - ord('a')] -= 1
                if inDegrees[ord(child) - ord('a')] == 0:
                    q.append(child)
                    res.append(child)
                    count += 1

        # all have gone into q then return res
        if count == len(hMap):
            return "".join(res)
        return ""

    def buildGraph(self, words, hMap, inDegrees):
        for word in words:  # O(n*l), l is avg len of each word
            for i in range(len(word)):
                c = word[i]
                if c not in hMap:
                    hMap[c] = set()
        # do the comparisons
        for i in range(len(words)-1):  # V+E
            first = words[i]
            second = words[i+1]
            if len(first) != len(second) and first.startswith(second):
                # clear the hMap so that count == 0
                # nothing added q
                hMap.clear()
                break
            low = 0
            if len(first) < len(second):
                low = len(first)
            else:
                low = len(second)
            for j in range(low):
                fChar = first[j]
                sChar = second[j]
                if fChar != sChar:
                    fSet = hMap[fChar]
                    if sChar not in fSet:
                        hMap[fChar].add(sChar)
                        inDegrees[ord(sChar) - ord('a')] += 1
                    # at the first mistmatch break
                    break
