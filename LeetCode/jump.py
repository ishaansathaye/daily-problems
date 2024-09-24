from typing import List
from collections import deque


class Solution:
    def jump2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums)
        q = deque()
        hSet = set()
        q.append(0)
        hSet.add(0)
        jumps = 0
        while len(q) != 0:
            # need size since level by level
            size = len(q)
            for i in range(0, size):
                # popleft removes from front
                # since using deque not array anymore
                currIdx = q.popleft()
                for j in range(1, nums[currIdx]+1):
                    child = currIdx + j
                    if child >= n-1:
                        return jumps+1
                    if child not in hSet:
                        q.append(child)
                        hSet.add(child)
            # each level is a jump
            jumps += 1
        return jumps

    def jump1(self, nums: List[int]) -> int:
        '''Optimized DFS'''
        self.dpMap = {}
        if len(nums) == 1:
            return 0
        return self.dfs(nums, 0)

    def dfs(self, nums, idx):
        # base
        if idx >= len(nums)-1:
            return 0
        # base 2
        if idx in self.dpMap:
            return self.dpMap[idx]
        # logic
        minJumps = 2**31
        for j in range(1, nums[idx]+1):
            child = idx + j
            minJumps = min(minJumps, self.dfs(nums, child))
        self.dpMap[idx] = minJumps+1
        return minJumps + 1

    def jump(self, nums: List[int]) -> int:
        '''Intervals Greedy Solution'''
        if len(nums) == 1:
            return 0
        jumps = 1
        currInterval = nums[0]
        nextInterval = nums[0]
        for i in range(0, len(nums)):
            # trying to go higher range element
            # always exploring better range elements
            nextInterval = max(nextInterval, i+nums[i])
            if i == currInterval:
                if i != len(nums) - 1:
                    jumps += 1
                currInterval = nextInterval
        return jumps
