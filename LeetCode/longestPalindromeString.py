class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_sub = s[0]
        if len(s) > 1:
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    substring = s[i:j+1]
                    if substring == substring[::-1] and len(substring) > 1 and len(substring) > len(max_sub):
                        max_sub = substring
        return max_sub

temp = Solution()
print(temp.longestPalindrome("babad"))
print(temp.longestPalindrome("a"))
print(temp.longestPalindrome("bb"))