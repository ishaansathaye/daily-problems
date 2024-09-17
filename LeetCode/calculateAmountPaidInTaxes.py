from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0.0
        i = 0  # idx on bracket
        lowerBound = 0  # prev value
        while income > 0:
            currBracket = brackets[i]
            upperBound = currBracket[0]
            perc = currBracket[1]
            # what is lower: remaining $ or amount of range
            taxableIncome = min(upperBound-lowerBound, income)
            res += taxableIncome*(perc/100)
            income -= taxableIncome
            i += 1
            lowerBound = upperBound
        return res
