class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # taking care of range of values in constraints
        if dividend == -2**31 and divisor == -1:
            return 2**31-1

        # java work with longs since might overshoot int
        ldividend = abs(dividend)
        ldivisor = abs(divisor)
        res = 0
        while ldividend >= ldivisor:
            shifts = 0
            while ldividend >= ldivisor << shifts:
                shifts += 1
            shifts -= 1  # go one step back
            # 1 more outer loop run if still >=:
            ldividend = ldividend - (ldivisor << shifts)
            # update res with current quotient
            res += 1 << shifts  # 2**shifts

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return -res
        return res
