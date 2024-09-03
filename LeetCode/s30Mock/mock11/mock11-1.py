from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        n = len(tokens)
        for i in range(n):
            if tokens[i] == "+":
                sec = st.pop()
                first = st.pop()
                st.append(first+sec)
            elif tokens[i] == "-":
                sec = st.pop()
                first = st.pop()
                st.append(first-sec)
            elif tokens[i] == "*":
                sec = st.pop()
                first = st.pop()
                st.append(first*sec)
            elif tokens[i] == "/":
                sec = st.pop()
                first = st.pop()
                st.append(int(first/sec))
            else:
                st.append(int(tokens[i]))
        return st.pop()
