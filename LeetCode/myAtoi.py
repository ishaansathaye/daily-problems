class Solution:
    def myAtoi(self, s: str) -> int:
        '''Original'''
        neg = False
        num = 0
        s = s.strip()
        if not s:
            return 0
        if s[0] == '-':
            neg = True
            start = 1
        elif s[0] == '+':
            start = 1
        else:
            start = 0

        for i in range(start, len(s)):
            if s[i].isdigit():
                num = num*10 + (ord(s[i]) - ord('0'))
                if num >= 2**31 and neg:
                    return -2**31
                if num >= 2**31:
                    return 2**31 - 1
            else:
                break

        if self.neg:
            return num*-1
        return num

    def myAtoi(self, s: str) -> int:
        '''s30'''
        res = 0
        sign = True  # positive
        s = s.strip()
        if not s:
            return 0
        first = s[0]
        if first != '-' and first != '+' and not first.isdigit():
            return res
        if first == '-':
            sign = False
        limit = (2**31-1)//10
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                currDigit = ord(ch) - ord('0')
                if sign:
                    # never going beyond 10 digits
                    if res > limit:
                        return 2**31 - 1
                    elif (res == limit):
                        # if incoming is > 7
                        if currDigit > 7:
                            return 2**31 - 1
                else:
                    # never going beyond 10 digits
                    if res > limit:
                        return -2**31
                    elif (res == limit):
                        # if incoming is > 8
                        if currDigit > 8:
                            return -2**31
                res = res*10 + currDigit
            elif i != 0:
                break
        if sign:
            return res
        return -res
