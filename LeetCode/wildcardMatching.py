class Solution:
    def __isMatch(self, s: str, p: str) -> bool:
        '''Regular Expression Solution'''
        '''DP -> O(mxn) both'''
        if s == p or p == "*":
            return True
        sl = len(s)
        pl = len(p)

        dp = [[False for _ in range(pl+1)] for _ in range(sl+1)]
        dp[0][0] = True
        for j in range(1, pl+1):
            if p[j-1] == '*':
                # if star and at top just look at prev val
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = False
        for i in range(1, sl+1):
            for j in range(1, pl+1):
                # star case
                if p[j-1] == '*':
                    # 0 and 1 case
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    if p[j-1] == '?' or p[j-1] == s[i-1]:
                        # look at diag up
                        dp[i][j] = dp[i-1][j-1]
        return dp[sl][pl]

    def _isMatch(self, s: str, p: str) -> bool:
        '''Regular Expression Solution'''
        '''DP -> O(mxn)'''
        if s == p or p == "*":
            return True
        sl = len(s)
        pl = len(p)

        dp = [False for _ in range(pl+1)]
        dp[0] = True
        for j in range(1, pl+1):
            if p[j-1] == '*':
                # if star and at top just look at prev val
                dp[j] = dp[j-1]

        for i in range(1, sl+1):
            # diagUp = False
            # if i == 1:
            #     diagUp = True
            diagUp = dp[0]
            dp[0] = False
            for j in range(1, pl+1):
                temp = dp[j]
                # star case
                if p[j-1] == '*':
                    # 0 and 1 case
                    dp[j] = dp[j-1] or dp[j]
                else:
                    if p[j-1] == '?' or p[j-1] == s[i-1]:
                        # look at diag up
                        dp[j] = diagUp
                    else:
                        dp[j] = False
                diagUp = temp
        return dp[pl]

    def isMatch(self, s: str, p: str) -> bool:
        '''Avg Case: O(n)'''
        if s == p or p == "*":
            return True
        sl = len(s)
        pl = len(p)
        sp = 0
        pp = 0
        pStar = -1
        sStar = -1

        while sp < sl:
            if pp < pl and (p[pp] == s[sp] or p[pp] == '?'):
                sp += 1
                pp += 1
            elif pp < pl and p[pp] == '*':
                # assume the 0 case
                sStar = sp
                pStar = pp
                pp += 1
            elif sStar == -1:
                # star has never happened
                return False
            else:
                pp = pStar + 1
                # 1 cases
                # skip the character(s) to be replaced by *
                sStar += 1
                # move sp pointer to that character
                sp = sStar

        while pp < pl:
            if p[pp] != '*':
                return False
            pp += 1
        return True
