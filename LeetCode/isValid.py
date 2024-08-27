class Solution:
    def isValid(self, s: str) -> bool:
        st = []  # of characters
        for i in range(len(s)):
            c = s[i]
            # everytime you see opening put a closing
            if c == '[':
                st.append(']')
            elif c == '{':
                st.append('}')
            elif c == '(':
                st.append(')')
            else:
                # if one of closing types
                if len(st) == 0 or st.pop() != c:
                    return False
        if len(st) != 0:
            return False
        return True
