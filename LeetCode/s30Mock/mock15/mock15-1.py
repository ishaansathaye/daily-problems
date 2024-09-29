from typing import List
from collections import defaultdict


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        map1 = defaultdict(str)  # indices : target
        map2 = defaultdict(list)  # indices : not len(source) -> end
        for i in range(len(indices)):
            end = len(sources[i]) + indices[i]
            if sources[i] == s[indices[i]:end]:
                map1[indices[i]] = targets[i]
                # need start index to end mapping
                # not target string to end
                map2[indices[i]] = end

        res = []
        k = 0
        n = len(s)
        while k < n:
            if k in map1:
                res.append(map1[k])
                # which index to start at next
                k = map2[k]
            else:
                res.append(s[k])
                k += 1

        return "".join(res)
