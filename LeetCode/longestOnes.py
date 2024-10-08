from typing import List


class Solution:
    def _longestOnes(self, nums: List[int], k: int) -> int:
        '''Sliding Window'''
        low = 0
        count = 0
        n = len(nums)
        # i is the high pointer
        maxRange = 0
        for i in range(n):
            if nums[i] == 0:
                count += 1
                if count > k:
                    # slide the window to escape prev zero
                    while nums[low] != 0:
                        low += 1
                    low += 1  # escape that zero
                    count -= 1
            # find the length
            maxRange = max(maxRange, i-low+1)
        return maxRange

    def longestOnes(self, nums: List[int], k: int) -> int:
        '''Optimized Sliding Window -> O(n) perfectly'''
        low = 0
        count = 0
        n = len(nums)
        # i is the high pointer
        for i in range(n):
            if nums[i] == 0:
                count += 1
            if count > k:
                if nums[low] == 0:
                    count -= 1
                low += 1
        return n-low
