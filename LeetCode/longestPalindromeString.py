class Solution:
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
    
    #create solution that finds biggest substring among original and flipped


temp = Solution()
# print(temp.longestPalindrome("babad"))
# print(temp.longestPalindrome("a"))
# print(temp.longestPalindrome("bb"))
# print(temp.longestPalindrome("cbbd"))
# print(temp.longestPalindrome("abb"))
# print(temp.longestPalindrome("xaabacxcabaaxcabaax"))
print(temp.longestPalindrome("abbcccbbbcaaccbababcbcabca"))