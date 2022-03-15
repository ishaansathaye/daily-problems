class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #118 ms
        char_dict = {}
        curr_substr = ""
        max_length = 0
        for i in range(len(s)):
            if s[i] in char_dict and char_dict[s[i]][0] >= 1:
                if curr_substr[0] == s[i]:
                    curr_substr = curr_substr[1:]
                    curr_substr += s[i]
                    char_dict[s[i]][1] = i
                elif curr_substr[-1] == s[i]:
                    curr_substr = s[i]
                    char_dict = {}
                    char_dict[s[i]] = [1, i]
                else:
                    position = char_dict[s[i]][1] + 1
                    index = curr_substr.index(s[i])
                    for j in range(0, index+1):
                        del char_dict[curr_substr[j]]
                    curr_substr = s[position:i]
                    curr_substr += s[i]
                    char_dict[s[i]] = [1,i]
            else:
                curr_substr += s[i]
                char_dict[s[i]] = [1, i]
            max_length = max(len(curr_substr), max_length)
        return max_length

    #Approach 1: Sliding Window --> O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128 #uses ascii value to define a "hash map"

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res

    #Approach 2: Sliding Window Optimized --> O(n) --> less steps
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

                

temp = Solution()
print(temp.lengthOfLongestSubstring("abcabcbb")) #3
print(temp.lengthOfLongestSubstring("bbbbb")) #1
print(temp.lengthOfLongestSubstring("pwwkew")) #3
print(temp.lengthOfLongestSubstring(" ")) #1
print(temp.lengthOfLongestSubstring("")) #0
print(temp.lengthOfLongestSubstring("tmmzuxt")) #5
print(temp.lengthOfLongestSubstring("wobgrovw")) #6
print(temp.lengthOfLongestSubstring("eeydgwdykpv")) #6
