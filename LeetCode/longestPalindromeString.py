class Solution:
    # time limit exceeded
    def ___longestPalindrome(self, s: str) -> str:
        pal = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(pal):
                    pal = s[i:j+1]
        return pal

    def _longestPalindrome(self, s: str) -> str:
        '''Expand Pointers Solution'''
        self.start = 0
        self.end = 0
        self.n = len(s)
        self.res = ""
        for i in range(self.n):
            # each char as a potential middle
            # expanding at each char
            self.expand(s, i, i)  # O(n)
            if i < self.n-1 and s[i] == s[i+1]:
                # consec chars eq -> even len pali check
                self.expand(s, i, i+1)  # O(n)
        return s[self.start:self.end+1]

    def expand(self, s, left, right):
        while left >= 0 and right < self.n and s[left] == s[right]:
            left -= 1
            right += 1
        left += 1
        right -= 1
        if right - left > self.end - self.start:
            self.start = left
            self.end = right

    def __longestPalindrome(self, s: str) -> str:
        '''DP'''
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        start = 0
        end = 0
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    # have length less than 2
                    # or between substring is True
                    if i - j < 2 or dp[i-1][j+1]:
                        dp[i][j] = True
                        # make new start and end
                        if i - j > end - start:
                            start = j
                            end = i
                    # else:
                    #     dp[i][j] = False
        return s[start:end+1]

    def longestPalindrome(self, s: str) -> str:
        '''DP - Space Optimized'''
        n = len(s)
        dp = [False for _ in range(n)]
        start = 0
        end = 0
        for i in range(n):
            # flipped loop to save state of arr
            # up right is saved going from left to right
            for j in range(0, i+1):
                if s[i] == s[j]:
                    # right up is just on right hand side
                    if i - j < 2 or dp[j+1]:
                        dp[j] = True
                        # make new start and end
                        if i - j > end - start:
                            start = j
                            end = i
                    else:
                        dp[j] = False
                else:
                    dp[j] = False
        return s[start:end+1]


temp = Solution()
print(temp.longestPalindrome("babad"))
print(temp.longestPalindrome("a"))
print(temp.longestPalindrome("bb"))
print(temp.longestPalindrome("cbbd"))
print(temp.longestPalindrome("abb"))
print(temp.longestPalindrome("xaabacxcabaaxcabaax"))
print(temp.longestPalindrome("abbcccbbbcaaccbababcbcabca"))
