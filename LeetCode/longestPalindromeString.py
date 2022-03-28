class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     max_sub = s[0]
    #     if len(s) > 1:
    #         for i in range(len(s)):
    #             for j in range(i+1, len(s)):
    #                 substring = s[i:j+1]
    #                 if substring == substring[::-1] and len(substring) > 1 and len(substring) > len(max_sub):
    #                     max_sub = substring
    #     return max_sub
    
    def longestPalindrome(self, s: str, max_str="") -> str:
        if len(s) == 0:
            return max_str
        if len(s) == 1 and len(s) > len(max_str):
            return s
        if s == s[::-1] and len(s) > len(max_str):
            return s
        end = len(s)
        for i in range(len(s)):
            if len(max_str) >= len(s[i:end-1]):
                return max_str
            else:
                max_str = self.longestPalindrome(s[i:end-1], max_str)
            end = len(s)+1
        return max_str


temp = Solution()
# print(temp.longestPalindrome("babad"))
# print(temp.longestPalindrome("a"))
# print(temp.longestPalindrome("bb"))
# print(temp.longestPalindrome("cbbd"))
# print(temp.longestPalindrome("abb"))
# print(temp.longestPalindrome("xaabacxcabaaxcabaax"))
print(temp.longestPalindrome("abbcccbbbcaaccbababcbcabca"))