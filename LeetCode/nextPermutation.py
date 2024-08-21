from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return
        n = len(nums)
        i = n-2
        # find the breach
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # find the digit to swap ith breach digit with
        if i >= 0:
            j = n-1
            while nums[i] >= nums[j]:
                j -= 1
            self.swap(nums, i, j)
        # reverse the smallest of digits from i+1
        self.reverse(nums, i+1, n-1)

    def reverse(self, nums, left, right):
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
