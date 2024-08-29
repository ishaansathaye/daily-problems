from typing import List
import deque


class Solution:
    def canJump3(self, nums: List[int]) -> bool:
        '''BFS'''
        if len(nums) < 2:
            return True
        q = deque()
        visited = set()
        q.append(0)
        visited.add(0)
        while len(q) != 0:
            idx = q.pop()
            # for loop is the jumps till max idx
            for j in range(1, nums[idx]+1):
                newIdx = idx+j
                if newIdx == len(nums)-1:
                    return True
                if newIdx not in visited:
                    q.append(newIdx)
                    visited.add(newIdx)
        return False

    def canJump2(self, nums: List[int]) -> bool:
        '''DFS'''
        return self.dfs(nums, 0)

    def dfs(self, nums, idx):
        # base
        if idx >= len(nums)-1:
            return True
        # logic
        for i in range(1, nums[idx]+1):
            newIdx = idx + i
            if self.dfs(nums, newIdx):
                return True
        return False

    def canJump1(self, nums: List[int]) -> bool:
        '''Optimized DFS with DP'''
        '''Both bfs and this are top-down DP'''
        self.dpSet = set()
        return self._dfs(nums, 0)

    def _dfs(self, nums, idx):
        # base
        if idx >= len(nums)-1:
            return True
        # logic
        for i in range(1, nums[idx]+1):
            newIdx = idx + i
            if newIdx in self.dpSet:
                continue
            if self._dfs(nums, newIdx):
                return True
        # only adding into set if path gives a false
        self.dpSet.add(idx)
        return False

    def canJump(self, nums: List[int]) -> bool:
        '''Greedy Solution from Back'''
        # start with target as the end of the arr
        target = len(nums) - 1
        n = len(nums)
        for i in range(n-2, -1, -1):
            # idx+element can breach the target index
            if i+nums[i] >= target:
                # yes then make i the target index
                target = i
        # check if we have reached the start
        return target == 0

    def _canJump(self, nums: List[int]) -> bool:
        '''Interval Greedy Solution'''
        if len(nums) < 2:
            return True
        currInterval = nums[0]
        nextInterval = nums[0]
        # cannot go anywhere if 0
        if nextInterval == 0:
            return False
        for i in range(0, len(nums)):
            nextInterval = max(nextInterval, i + nums[i])
            # if curr and next stuck at same then just return False
            if (i == currInterval and nextInterval == currInterval
                    and i != len(nums)-1):
                return False
            # if next interval has more than breached just return True
            if i != len(nums) - 1 and nextInterval >= len(nums)-1:
                return True
            # if reached the end of currInterval go to next one
            if currInterval == i:
                currInterval = nextInterval
        if nextInterval >= len(nums)-1:
            return True
        return False
