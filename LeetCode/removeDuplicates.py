from collections import deque


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''Stack'''
        st = deque()  # character stack only
        numSt = deque()  # count stack only
        for i in range(len(s)):
            ch = s[i]
            if len(st) != 0 and st[-1] == ch:
                count = numSt.pop()
                count += 1
                if count == k:
                    st.pop()
                else:
                    numSt.append(count)
            else:
                st.append(ch)
                numSt.append(1)

        sb = []
        while len(st) != 0:
            count = numSt.pop()
            currChar = st.pop()
            for i in range(count):
                sb.append(currChar)
        return "".join(sb[::-1])
