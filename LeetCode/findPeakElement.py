from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high-low) // 2
            # at idx 0 -> has to greater than idx+1
            # at idx len(nums) - 1 -> has to be greater than idx-1
            if ((mid == 0 or nums[mid] > nums[mid-1]) and
                    (mid == len(nums)-1 or nums[mid] > nums[mid+1])):
                return mid
            # move left if left neighbor is greater
            elif mid > 0 and nums[mid] < nums[mid-1]:
                high = mid-1
            # move right if right neighbor is greater
            else:
                low = mid+1


if __name__ == "__main__":
    s = Solution()
    print(s.findPeakElement([1, 2, 3, 1]))
