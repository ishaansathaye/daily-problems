from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''Taking XOR of each element'''
        res = 0
        for i in nums:
            res = res ^ i
        return res
