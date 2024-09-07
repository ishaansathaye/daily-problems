from typing import List


class Solution:
    def numberOfArithmeticSlices2(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n-2):
            diff = nums[i+1]-nums[i]
            for j in range(i+2, n):
                if nums[j]-nums[j-1] == diff:
                    count += 1
                else:
                    break
        return count

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''DP Array'''
        count = 0
        n = len(nums)
        dp = [0]*n
        for i in range(n-3, -1, -1):
            if nums[i+1]-nums[i] == nums[i+2]-nums[i+1]:
                dp[i] = dp[i+1] + 1
            else:
                dp[i] = 0
            count += dp[i]
        return count

    def _numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''1 Var Algo'''
        count = 0
        n = len(nums)
        curr = 0
        for i in range(n-3, -1, -1):
            if nums[i+1]-nums[i] == nums[i+2]-nums[i+1]:
                # use just 1 var
                # since only using count to the right of current
                curr += 1
            else:
                curr = 0
            count += curr
        return count
