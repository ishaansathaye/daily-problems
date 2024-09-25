from collections import defaultdict
from bisect import bisect_left


class Solution:
    def _shortestWay(self, source: str, target: str) -> int:
        '''Brute Force: Pointers'''
        hSet = set(source)  # O(1) space
        n = len(source)
        m = len(target)

        i = 0  # target
        j = 0  # source
        # have started using subsequence of source
        count = 1  # if abc and abc
        while i < m:  # O(m*n)
            if j >= n:
                count += 1
                j = 0
            tChar = target[i]
            if tChar not in hSet:
                return -1
            if tChar == source[j]:
                j += 1
                i += 1
            else:
                j += 1

        return count

    def shortestWay(self, source: str, target: str) -> int:
        '''Binary Search to reduce source lookup -> O(mlogk)'''
        hMap = defaultdict(list)
        n = len(source)
        m = len(target)
        # put into hMap
        for i in range(n):
            c = source[i]
            hMap[c].append(i)
        sp = 0
        tp = 0
        count = 1
        while tp < m:
            tChar = target[tp]
            if tChar not in hMap:
                return -1
            li = hMap[tChar]
            # find using BS the exact index
            # or index just greater than sp
            k = bisect_left(li, sp)
            # or
            # k = self.binarySearch(li, sp)

            # 3 cases to consider:
            # if we do find exact index in li
            # if we do not find exact idx in li
            # if we go out of bounds

            # out of bounds
            if k == len(li):
                count += 1
                # move source to first occurrence
                sp = li[0]
            else:
                # move sp to right position for char check
                sp = li[k]
            tp += 1
            sp += 1
        return count

    def binarySearch(self, li, target):
        # logic
        low = 0
        high = len(li)-1
        while low <= high:
            mid = low + (high - low) // 2
            if li[mid] == target:
                return mid
            elif li[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
