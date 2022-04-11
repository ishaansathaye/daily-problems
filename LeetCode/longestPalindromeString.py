class Solution:
    #time limit exceeded
    def longestPalindrome(self, s: str) -> str:
        pal = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(pal):
                    pal = s[i:j+1]
        return pal
    
    #TODO: write solution for finding common substring between reversed and original string


temp = Solution()
print(temp.longestPalindrome("babad"))
print(temp.longestPalindrome("a"))
print(temp.longestPalindrome("bb"))
print(temp.longestPalindrome("cbbd"))
print(temp.longestPalindrome("abb"))
print(temp.longestPalindrome("xaabacxcabaaxcabaax"))
print(temp.longestPalindrome("abbcccbbbcaaccbababcbcabca"))