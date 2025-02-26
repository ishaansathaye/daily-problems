from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        if not digits:
            return []

        res = []
        self.backtrack(digits, 0, "", res)
        return res

    def backtrack(self, digits, idx, comb, res):
        # base case
        if idx >= len(digits):
            res.append(comb)
            return

        # logic
        currMap = self.mapping[digits[idx]]
        for c in currMap:
            # action
            comb += c
            # recurse
            self.backtrack(digits, idx+1, comb, res)
            # backtrack
            comb = comb[0:len(comb)-1]
