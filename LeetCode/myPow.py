class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if n == 0:
            return 1

        # if n is negative then flip x
        # make n positive
        if n < 0:
            x = 1/x
            n = -n

        res = self.myPow(x, n//2)

        if n % 2 == 0:
            return res*res
        else:
            return res*res*x

    def _myPow(self, x: float, n: int) -> float:
        '''Iterative Approach'''
        res = 1
        # negative case:
        if n < 0:
            x = 1/x
            n = -n

        while n > 0:
            if n % 2 != 0:
                res = res * x
            x = x*x
            n = n//2
        return res
