from typing import List


def searchRange(nums: List[int]) -> int:
    # null case
    low = 0
    high = len(nums) - 1
    while (low <= high):
        if (nums[low] <= nums[high]):  # complete range is sorted
            return nums[low]
        mid = low + (high - low) // 2
        # is mid is the min
        if (mid > 0 and nums[mid] < nums[mid-1]):  # also can put != for [2, 1]
            return nums[mid]
        elif (nums[low] <= nums[mid]):  # is left sorted
            low = mid + 1
        else:
            high = mid - 1
            # high = mid for (low < high) in while statement
    # return nums[low] for while statement
