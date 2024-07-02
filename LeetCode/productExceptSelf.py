from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0 for i in range(n)]
    rp = 1
    result[0] = rp
    # left to right
    for i in range(1, n):
        rp = rp*nums[i-1]
        result[i] = rp
    # left products in arr
    rp = 1
    # right to left
    # n-2, <= 0, i-- in java
    for i in range(n-2, -1, -1):  # do this b/c ends are 1
        rp = rp*nums[i+1]
        # multiply the current left product with the running right product
        result[i] = result[i]*rp
    return result


print(productExceptSelf([1, 2, 3, 4]))
