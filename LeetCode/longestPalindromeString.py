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
    def longestPalindrome(self, s: str, max_str="") -> str:
        flipped = s[::-1]
        ans_long = ""
        pal = ""
        curr_char = {}

        i = 0
        for j in range(len(s)):
            if s[j] in curr_char:
                i = max(curr_char[s[j]], i)
            if len(s[i:j+1]) > len(ans_long):
                ans_long = s[i:j+1]
                if s[i:j+1] == flipped[i:j+1]:
                    pal = s[i:j+1]
            curr_char[s[j]] = j+1
        return pal


temp = Solution()
print(temp.longestPalindrome("babad"))
print(temp.longestPalindrome("a"))
print(temp.longestPalindrome("bb"))
print(temp.longestPalindrome("cbbd"))
print(temp.longestPalindrome("abb"))
print(temp.longestPalindrome("xaabacxcabaaxcabaax"))
print(temp.longestPalindrome("abbcccbbbcaaccbababcbcabca"))