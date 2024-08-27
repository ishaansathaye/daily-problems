from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []  # of indices
        n = len(nums)
        res = [-1 for _ in range(n)]  # O(n)
        # 2 times since circular
        for i in range(2*n):  # O(3n)
            # ensure not out of bounds
            idx = i % n
            while len(st) != 0 and nums[idx] > nums[st[-1]]:
                popped = st.pop()
                res[popped] = nums[idx]
            # only put in stack in the first n traversal
            if i < n:
                st.append(idx)
        return res
