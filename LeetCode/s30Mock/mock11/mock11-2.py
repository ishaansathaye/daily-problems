class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        n = len(num)
        st = []
        count = 0
        for i in range(n):
            while len(st) != 0 and count != k and int(st[-1]) > int(num[i]):
                count += 1
                st.pop()
            st.append(num[i])

        while len(st) != 0 and count < k:
            count += 1
            st.pop()

        while len(st) != 0 and st[0] == "0":
            st.pop(0)

        res = ""
        while len(st) != 0:
            res = st.pop() + res
        return "0" if res == "" else res[0:n-k]
