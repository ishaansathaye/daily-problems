from typing import List
from functools import cmp_to_key


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''O(nlogn)'''
        def sort(a, b):
            # split with 1 as maxSplit with create 2 entries
            strArr1 = a.split(" ", 1)
            strArr2 = b.split(" ", 1)
            # checking if digit log or not
            isDigit1 = strArr1[1][0].isdigit()
            isDigit2 = strArr2[1][0].isdigit()
            if not isDigit1 and not isDigit2:
                if strArr1[1] != strArr2[1]:
                    return -1 if strArr1[1] < strArr2[1] else 1
                return -1 if strArr1[0] < strArr2[0] else 1
            elif isDigit1 and not isDigit2:
                # bring the second 1 front of first one
                return 1
            elif not isDigit1 and isDigit2:
                # keep the first one if front
                return -1
            else:
                # retain order if both digit logs
                return 0

        logs = sorted(logs, key=cmp_to_key(sort))
        return logs
