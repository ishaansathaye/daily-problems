class Solution:
    def _isHappy(self, n: int) -> bool:
        '''Original'''
        hMap = {}
        while True:
            orig = str(n)
            n = 0
            for i in range(len(orig)):
                n += int(orig[i])**2
            if str(n) in hMap:
                return False
            if n == 1:
                return True
            hMap[orig] = n
        return True

    def isHappy(self, n: int) -> bool:
        '''Using Set and No Type Conversions'''
        hSet = set()
        while n != 1 and n not in hSet:
            hSet.add(n)
            newN = 0
            rem = 0
            while n > 0:
                rem = n % 10  # get remainder
                n = n // 10   # get new n after removing digit
                newN += rem**2
            n = newN
        return n == 1


'''
19%10 = 9
19//10 = 1
divmod(19,10) -> (1, 9)
divmod(1, 10) -> (0, 1)

'''
