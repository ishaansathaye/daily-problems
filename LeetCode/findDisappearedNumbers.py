from typing import List

# ask interviewer if the array can be changed


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    result = []
    n = len(nums)
    for i in range(n):
        currNum = abs(nums[i])
        idx = currNum - 1
        if nums[idx] > 0:
            nums[idx] *= -1
    for i in range(n):  # find the values that are positive
        if nums[i] > 0:
            result.append(i+1)  # add value at that +1
    return result
