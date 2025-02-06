from typing import List
from collections import deque
import heapq as hq


class Solution:
    '''Does not work, have to keep track on indices of max and min'''
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     left = 0
    #     right = 0
    #     maxNum = nums[0]
    #     minNum = nums[0]
    #     maxLen = 1
    #     while left < len(nums) and right < len(nums)-1 and left <= right:
    #         right += 1
    #         maxNum = max(maxNum, nums[right])
    #         minNum = min(minNum, nums[right])
    #         if abs(maxNum-minNum) <= limit:
    #             maxLen += 1
    #         else:
    #             left += 1
    #             minNum = min(nums[left], nums[right])
    #             maxNum = max(nums[left], nums[right])
    #     return maxLen

    def _longestSubarray(self, nums: List[int], limit: int) -> int:
        '''Min and Max Heap Approach: O(nlogn), O(n)'''
        minHeap = []
        maxHeap = []
        left = 0
        maxLen = 0

        for right in range(len(nums)):
            hq.heappush(minHeap, (nums[right], right))
            hq.heappush(maxHeap, (-nums[right], right))

            # print("Added to both maxHeap:", maxHeap)
            # print("Added to both minHeap:", minHeap)
            # print()

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                # print("Inside while maxHeap:", maxHeap)
                # print("Inside while minHeap:", minHeap)
                # print()
                # moving left pointer to right
                # until condition is satisfied
                # essentially removing element that caused this
                left = min(maxHeap[0][1], minHeap[0][1]) + 1

                # remove elements from heaps outside of window
                while maxHeap[0][1] < left:
                    hq.heappop(maxHeap)
                    # print("maxHeap:", maxHeap)
                while minHeap[0][1] < left:
                    hq.heappop(minHeap)
                #     print("minHeap:", minHeap)
                # print("max outside:", maxHeap)
                # print("min outside:", minHeap)

            maxLen = max(maxLen, right-left+1)

        return maxLen

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''2 Deque Approach: O(n), O(n)'''
        minQ = deque()
        maxQ = deque()
        left = 0
        maxLen = 0

        for right in range(len(nums)):
            # maintain decreasing order in maxQ
            while maxQ and maxQ[-1] < nums[right]:
                maxQ.pop()
            maxQ.append(nums[right])

            # maintain increasing order in minQ
            while minQ and minQ[-1] > nums[right]:
                minQ.pop()
            minQ.append(nums[right])

            # move left pointer until condition satisfied
            while maxQ[0] - minQ[0] > limit:
                # removing elements out of current window
                if maxQ[0] == nums[left]:
                    maxQ.popleft()
                if minQ[0] == nums[left]:
                    minQ.popleft()
                left += 1

            maxLen = max(maxLen, right-left+1)
        # print(left)
        return maxLen


'''
10 1 2 4 7 2
limit = 5

8 2 4 7
limit = 4

[1,5,6,7,8,10,6,5,6]
limit = 4
answ = 5

left = 6
right = 7
maxHeap: 10,5 8,4 7,3 6,2 | 6,6 5,1, 5,7 1,0
minHeap: 1,0 5,1 | 5,7 6,2 6,6 7,3 8,4 10,5

maxQ: 1 | 5 | 6 | 7 | 8 | 10 | 6 6
minQ: 1 | 5 | 6 7 8 9 10 | 6 6 | 5 6
left = 6

'''

if __name__ == '__main__':
    s = Solution()
    nums = [10, 1, 2, 4, 7, 2]
    nums2 = [8, 2, 4, 7]
    nums3 = [1, 5, 6, 7, 8, 10, 6, 5, 6]
    assert s.longestSubarray(nums, 5) == 4
    assert s.longestSubarray(nums2, 4) == 2
    assert s.longestSubarray(nums3, 4) == 5
    assert s.longestSubarray([8, 5, 6, 2, 3, 9], 3) == 3
