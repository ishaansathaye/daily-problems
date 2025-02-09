from typing import List


class Solution:
    def _minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''Original: O(n)'''
        if nums == []:
            return 0
        left = 0
        right = 0
        minLen = len(nums)+1
        rollingSum = nums[right]
        while right <= len(nums):
            if rollingSum < target:
                right += 1
                if right < len(nums):
                    rollingSum += nums[right]
            elif rollingSum >= target:
                minLen = min(minLen, right-left+1)
                rollingSum -= nums[left]
                left += 1
        return 0 if minLen == len(nums)+1 else minLen

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''Faster Solution still O(n)'''
        n = len(nums)
        res = n + 1
        right = 0
        left = 0
        sum = 0
        while right < n:
            sum += nums[right]
            while sum >= target:
                res = min(res, right-left+1)
                sum -= nums[left]
                left += 1
            right += 1
        return res if res <= n else 0


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
    print(s.minSubArrayLen(4, [1, 4, 4]))
