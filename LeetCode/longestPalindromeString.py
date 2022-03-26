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
    
    def longestPalindrome(self, s: str) -> str:
        max_pal = ""
        current_str = ""
        for i in range(len(s)):
            current_str += s[i]
            if current_str == current_str[::-1]:
                if len(current_str) > len(max_pal):
                    max_pal = current_str
        return max_pal


temp = Solution()
print(temp.longestPalindrome("babad"))
print(temp.longestPalindrome("a"))
print(temp.longestPalindrome("bb"))
print(temp.longestPalindrome("cbbd"))