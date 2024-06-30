from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        low = 0
        high = len(nums) - 1
        while low <= high: # until they do not cross
            # mid = (low + high) / 2 would result in integer 
            # overflow (-2^31 to 2^31 - 1)
            # ex. low = 2^31 - 10 and high = 2^31 - 5, low + high will result 
            # in negative since outside integer range (in C)
            mid = low + (high - low) // 2
            if (nums[mid] == target):
                return mid
            else:
                # check if left sorted
                if nums[low] <= nums[mid]:
                    # check if target in range
                    if (nums[low] <= target and nums[mid] > target):
                        # reject right half
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if (nums[mid] < target and nums[high] >= target):
                        low = mid + 1
                    else:
                        high = mid - 1
          # if nums[low] == target return low, for if while loop is low < high
        return -1