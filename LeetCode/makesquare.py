from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        '''Exhaustive by Backtracking -> Exponential'''
        matchSum = 0
        for match in matchsticks:
            matchSum += match
        if matchSum % 4 != 0:
            return False
        side = matchSum//4
        # optimization #1:
        for match in matchsticks:
            if match > side:
                return False
        # optimization #2:
        # sort in descending order
        # fill side with biggest matchstick first
        matchsticks.sort(reverse=True)
        return self.backtrack(matchsticks, 0, [0]*4, side)

    def backtrack(self, matchsticks, idx, square, side):
        # base
        if idx == len(matchsticks):
            if (square[0] == side and square[1] == side
                    and square[3] == side):
                return True
            else:
                return False
        # logic
        # go over each side
        for i in range(4):
            if square[i] + matchsticks[idx] <= side:
                # can put if current matchstick +
                # curr amount on side <= allowed side len
                # action
                square[i] += matchsticks[idx]
                # recurse
                if self.backtrack(matchsticks, idx+1, square, side):
                    return True
                # backtrack
                square[i] -= matchsticks[idx]
        return False
