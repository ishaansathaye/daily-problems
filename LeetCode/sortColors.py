from typing import List


def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0
    mid = 0
    right = len(nums)-1
    while mid <= right:  # make sure they do not cross (can still be same idx)
        if nums[mid] == 0:
            swap(nums, mid, left)
            left += 1
            mid += 1
        elif nums[mid] == 2:
            swap(nums, mid, right)
            right -= 1
        else:
            mid += 1


def swap(nums, p1, p2):
    if p1 != p2:
        temp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = temp
