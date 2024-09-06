from typing import List


class Solution:
    '''DP Solution gives Time Limit Exceeded - O(n^2)'''

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''Binary Search Solution'''
        n = len(envelopes)
        # effective arr of just heights
        arr = [0]*n
        # ascending for widths
        # descending for heights
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # O(nlogn)
        le = 1
        arr[0] = envelopes[0][1]
        for i in range(1, n):
            # compare heights for longest increasing heights
            if envelopes[i][1] > arr[le-1]:
                arr[le] = envelopes[i][1]
                le += 1
            else:
                bsIdx = self.binarySearch(arr, 0, le-1, envelopes[i][1])
                arr[bsIdx] = envelopes[i][1]
        return le

    def binarySearch(self, arr, low, high, target):
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        # wherever low ends up is the idx we want
        # for smallest element greater than or
        # equal to target
        return low
