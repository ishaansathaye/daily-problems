from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    slow = 0
    count = 1  # current element count
    k = 2
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1  # reset counter since unique number
        if count <= k:  # set k to a number
            slow += 1  # move up slow to set element
            nums[slow] = nums[i]
    return slow+1  # return number of elements
