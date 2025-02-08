from typing import List


class Solution:
    def _removeElement(self, nums: List[int], val: int) -> int:
        '''Original Solution'''
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] == val and nums[right] != val:
                nums[left] = nums[right]
                nums[right] = val
                left += 1
                right -= 1
            elif nums[left] == val and nums[right] == val:
                right -= 1
            else:
                left += 1

        cnt = 0
        for n in nums:
            if n != val:
                cnt += 1
        return cnt

    def removeElement(self, nums: List[int], val: int) -> int:
        '''Simple Two Pointers'''
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left


'''
[2,1,1,4,6,12,1,1,4,3,1] val = 1
[2,3,4,4,6,12,1,1,1,1,1]

'''
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([2, 1, 1, 4, 6, 12, 1, 1, 4, 3, 1], 1))
    print(s.removeElement([3, 2, 2, 3], 3))
    print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
