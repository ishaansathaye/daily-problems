from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    n = len(nums)
    # (a,b) -> b - a is under the hood for sorting in descending order
    nums = sorted(nums)
    # two pointers approach
    for i in range(n-2):
        # outside duplication
        if nums[i] > 0:  # will never get any sum = 0 if greater than 0
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # two pointers
        left = i+1
        r = n-1
        while left < r:  # not equal because cannot reuse the same element
            sum = nums[i] + nums[left] + nums[r]
            if sum == 0:
                result.append([nums[i], nums[left], nums[r]])
                left += 1
                r -= 1
                # need to check base cond again cause mutating
                while left < r and nums[left] == nums[left-1]:
                    left += 1
                while left < r and nums[r] == nums[r+1]:
                    r -= 1
            elif sum > 0:
                r -= 1
            else:
                left += 1
    return result
