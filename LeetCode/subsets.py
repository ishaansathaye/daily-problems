from typing import List


class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        '''Creating Deep Copy: O(n*2^n)'''
        result = []
        self.helper1(nums, 0, [], result)
        return result

    def helper1(self, nums, idx, path, result):
        # base
        if idx == len(nums):
            result.append(path)
            return
        # logic
        # do not choose
        self.helper1(nums, idx+1, path.copy(), result)
        # choose
        path.append(nums[idx])
        self.helper1(nums, idx+1, path.copy(), result)
        # can reverse choose and not choose case
        # but need to create deep copy first and then add elem

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        '''0/1 Rec. Backtracking: O(2^n)'''
        result = []
        self.helper2(nums, 0, [], result)
        return result

    def helper2(self, nums, idx, path, result):
        # base
        # creating deep copy at every n/2 nodes
        if idx == len(nums):
            result.append(path.copy())
            return
        # logic
        # do not choose
        self.helper2(nums, idx+1, path, result)
        # choose
        path.append(nums[idx])
        self.helper2(nums, idx+1, path, result)
        # backtrack action -> do not need copy
        path.pop(len(path)-1)

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        '''For Loop Rec. Backtracking: O(2^n)'''
        result = []
        self.helper3(nums, 0, [], result)
        return result

    def helper3(self, nums, pivot, path, result):
        # base -> for loop takes care of out of bounds
        # adding path at every node:
        result.append(path.copy())
        # logic
        for i in range(pivot, len(nums)):
            path.append(nums[i])
            # i is moving here not pivot (new i becomes pivot)
            self.helper3(nums, i+1, path, result)
            path.pop(len(path)-1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''For Loops Only: O(n*2^n)'''
        result = []
        result.append([])
        for i in range(len(nums)):
            # need to keep size fixed since result changes
            le = len(result)
            # range(len(result)) -> takes initial snapshot of length using len
            for j in range(le):
                # pythonic solution here:
                # temp = result[j][:] # : creates new list
                # temp.append(nums[i])
                # result.append(temp)
                li = result[j].copy()
                li.append(nums[i])
                result.append(li)
        return result
