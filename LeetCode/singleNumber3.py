from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for i in range(len(nums)):
            bitmask = bitmask ^ nums[i]
        # right most least significant bit isolated with &
        # -bitmask gives 2s complement
        temp = bitmask & (-bitmask)
        bitmask2 = 0
        for i in range(len(nums)):
            if nums[i] & temp != 0:
                bitmask2 = bitmask2 ^ nums[i]
        return (bitmask2, bitmask ^ bitmask2)
