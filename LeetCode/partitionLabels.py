from typing import List
import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hMap = defaultdict()  # of type char:int
        for i in range(len(s)):
            c = s[i]
            hMap[c] = i
        # start and end of partitions
        start = 0
        end = 0
        for i in range(len(s)):
            c = s[i]
            # either end or char's last index
            end = max(end, hMap[c])
            if i == end:
                res.append(end-start+1)
                # reset start to next partition beginning
                start = i+1
        return res
