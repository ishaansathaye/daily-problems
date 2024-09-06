from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''DP - O(n^2)'''
        n = len(nums)
        dp = [1]*n  # fill with 1 since itself is increasing
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def _lengthOfLIS(self, nums: List[int]) -> int:
        '''Binary Search - O(nlogn)'''
        n = len(nums)
        arr = [0]*n
        arr[0] = nums[0]
        # open pos in effective arr
        le = 1
        for i in range(1, n):
            if nums[i] > arr[le-1]:
                # last idx of effective arr
                # put into last position
                arr[le] = nums[i]
                le += 1
            else:
                # replace the number
                # just gerater than nums[i] in arr
                bsIdx = self.binarySearch(arr, 0, le-1, nums[i])
                arr[bsIdx] = nums[i]
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
