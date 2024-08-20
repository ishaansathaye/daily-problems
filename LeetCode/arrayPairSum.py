from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''O(nlogn)'''
        # bucket sort if we know the range of numbers
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res
