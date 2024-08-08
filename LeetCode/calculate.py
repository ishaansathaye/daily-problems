class Solution:
    def calculate(self, s: str) -> int:
        '''Maintaing a Tail O(1) Space'''
        num = 0
        calc = 0
        tail = 0
        lastSign = '+'
        s = s.strip()
        n = len(s)
        for i in range(n):
            c = s[i]
            if c.isdigit():
                num = num*10 + ord(c) - ord('0')
            # handle last num and space
            if not c.isdigit() and c != ' ' or i == n-1:
                if lastSign == '+':
                    calc = calc + num
                    tail = num
                elif lastSign == '-':
                    calc = calc - num
                    tail = -num
                elif lastSign == '*':
                    calc = calc - tail + (tail*num)
                    tail = tail*num
                else:
                    # use int to truncate toward zero (not //)
                    calc = calc - tail + int(tail/num)
                    tail = int(tail/num)
                num = 0
                # last sign becomes current looking at
                lastSign = c
        return calc

    def _calculate(self, s: str) -> int:
        '''Stack Solution O(n) Space'''
        num = 0
        lastSign = '+'
        s = s.strip()
        n = len(s)
        st = []
        for i in range(n):
            c = s[i]
            if c.isdigit():
                num = num*10 + ord(c) - ord('0')
            # handle last num and space
            if not c.isdigit() and c != ' ' or i == n-1:
                if lastSign == '+':
                    st.append(num)
                elif lastSign == '-':
                    st.append(-num)
                elif lastSign == '*':
                    st.append(st.pop()*num)
                else:
                    st.append(int(st.pop()/num))
                num = 0
                lastSign = c

        calc = 0
        # go through entire stack and sum elements
        while len(st) != 0:
            calc += st.pop()
        return calc
