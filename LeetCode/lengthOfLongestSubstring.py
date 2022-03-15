class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
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

                

temp = Solution()
print(temp.lengthOfLongestSubstring("abcabcbb")) #3
print(temp.lengthOfLongestSubstring("bbbbb")) #1
print(temp.lengthOfLongestSubstring("pwwkew")) #3
print(temp.lengthOfLongestSubstring(" ")) #1
print(temp.lengthOfLongestSubstring("")) #0
print(temp.lengthOfLongestSubstring("tmmzuxt")) #5
print(temp.lengthOfLongestSubstring("wobgrovw")) #6
print(temp.lengthOfLongestSubstring("eeydgwdykpv")) #6
