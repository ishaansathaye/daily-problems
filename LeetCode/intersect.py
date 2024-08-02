from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''HashMap Solution'''
        hMap = {}
        res = []
        if len(nums1) < len(nums2):
            # always want the first one to be smaller
            # TRICK
            return self.intersect(nums2, nums1)

        for i in range(len(nums1)):
            if nums1[i] not in hMap:
                hMap[nums1[i]] = 0
            hMap[nums1[i]] += 1

        for j in range(len(nums2)):
            curr = nums2[j]
            if curr in hMap:
                res.append(curr)
                hMap[curr] -= 1
                if hMap[curr] == 0:
                    del hMap[curr]

        return res

    def _intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''Sorted 2 Pointer Solution'''
        nums1.sort()
        nums2.sort()
        res = []
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return res

    def __intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''Shrinking BS Range Solution'''
        # Trick to always have first arr as smaller one:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        nums1.sort()
        nums2.sort()
        res = []

        low = 0
        high = len(nums2)-1
        for i in range(len(nums1)):
            curr = nums1[i]
            # BS on the bigger one
            bsIndex = self.binarySearch(nums2, low, high, curr)
            if bsIndex != -1:
                res.append(curr)
                # shrinking search range
                low = bsIndex+1
        return res

    def binarySearch(self, arr, low, high, target):
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                # is the first occurance or the beginning of search range
                if mid == low or arr[mid] != arr[mid-1]:
                    print(mid)
                    return mid
                else:
                    # not the first occurannce so move high
                    high = mid - 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
