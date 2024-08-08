class Solution:
    def calculate(self, s: str) -> int:
        '''O(n) for both'''
        st = []  # of integers
        s = s.strip()
        n = len(s)
        num = 0
        lastSign = '+'

        for i in range(n):
            c = s[i]
            if c.isdigit():
                num = num*10 + ord(c) - ord('0')
            elif c == '(':
                if lastSign == '+':
                    st.append(1)
                else:
                    st.append(-1)
                st.append(2**31)
                num = 0
                lastSign = '+'
            elif c == ')':
                # find itermediate result up to opening
                if lastSign == '+':
                    st.append(num)
                else:
                    st.append(-num)

                # unwrap the stack
                inter = 0
                print(st)
                while st[-1] != 2**31:
                    inter += st.pop()
                st.pop()  # pop out the "opening bracket"
                popped = st.pop()  # operator
                inter = inter * popped  # multiply by + or -
                st.append(inter)
                num = 0
                lastSign = '+'
            elif not c.isdigit() and c != ' ':
                if lastSign == '+':
                    st.append(num)
                else:
                    st.append(-num)
                num = 0
                lastSign = c

        # last element -> need
        # b/c only append when get next operator or closing
        if s[n-1] != ')':
            if lastSign == '+':
                st.append(num)
            else:
                st.append(-num)
        calc = 0
        while len(st) != 0:
            calc += st.pop()
        return calc
