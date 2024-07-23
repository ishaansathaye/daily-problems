from typing import List


class Solution:
    def combinationSum1(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        '''Brute Force like Coin Change  - > O((m+n)2^m+n)'''
        result = []
        self.helper(candidates, 0, target, [], result)
        return result

    def helper1(self, candidates, idx, target, path, result):
        # base
        if target == 0:
            result.append(path)
            return
        if target < 0 or idx == len(candidates):
            return
        # logic
        # case do not choose
        # make new array list at each node which is why copy()
        self.helper(candidates, idx+1, target, path.copy(), result)
        # case choose
        path.append(candidates[idx])
        # make new array list at each node which is why copy()
        self.helper(candidates, idx, target -
                    candidates[idx], path.copy(), result)

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        '''Optimization: Backtracking -> O(2^m+n)'''
        result = []
        self.helper2(candidates, 0, target, [], result)
        return result

    def helper2(self, candidates, idx, target, path, result):
        # base
        if target == 0:
            # create deep copy at the time adding into result
            result.append(path.copy())  # keeping this constant to TC
            return
        if target < 0 or idx == len(candidates):
            return
        # logic
        # case do not choose
        self.helper(candidates, idx+1, target, path, result)
        # case choose
        # action
        path.append(candidates[idx])
        # recurse
        self.helper(candidates, idx, target-candidates[idx], path, result)
        # backtrack: reverse the action
        # can now use the same path list
        path.pop(len(path)-1)

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        '''For Loop Recursion and Backtracking'''
        result = []
        self.helper(candidates, 0, target, [], result)
        return result

    def helper(self, candidates, pivot, target, path, result):
        # base
        if target == 0:
            # started with nothing needs to end with nothing
            # so deep copy
            result.append(path.copy())
            return
        if target < 0 or pivot > len(candidates):
            # do not need the pivot check since
            # for loop takes care of it
            return

        # logic
        for i in range(pivot, len(candidates)):
            # action
            path.append(candidates[i])
            # recurse
            self.helper(candidates, i, target-candidates[i], path, result)
            # backtrack the action
            path.pop(len(path)-1)

# Tree Shape:
# Depths more in 0/1 recursion
# Widths more in for loop recursion
# Time Complexity will be the same: O(2^m+n)


# Change problem from combination to permutation
# - instead of i just put pivot at 0 always
# - in fact you do not need pivot at all
