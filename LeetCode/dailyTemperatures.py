from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []  # of indices
        res = [0 for i in range(n)]
        for i in range(n):
            while len(st) != 0 and temperatures[i] > temperatures[st[-1]]:
                popped = st.pop()
                res[popped] = i - popped
            st.append(i)
        return res
