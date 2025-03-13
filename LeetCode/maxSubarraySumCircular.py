from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # kadane's algo to find max subarray sum
        localSum = nums[0]
        maxSum = nums[0]
        minLocal = minSum = nums[0]
        n = len(nums)
        for i in range(1, n):
            localSum = max(nums[i], localSum+nums[i])
            maxSum = max(maxSum, localSum)

            minLocal = min(nums[i], minLocal+nums[i])
            minSum = min(minLocal, minSum)

        # find maxSum of the circular array
        # totalSum - minSum (maximize sum by minimizing "missing component")
        total = sum(nums)
        circularSum = total - minSum

        if maxSum < 0:
            return min(circularSum, maxSum)
        return max(circularSum, maxSum)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [5, -3, 5]
    s = Solution()
    print(s.maxSubarraySumCircular(nums))
