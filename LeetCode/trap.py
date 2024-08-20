from typing import List


class Solution:
    def trap2(self, height: List[int]) -> int:
        '''2 Pass Solution'''
        n = len(height)
        # Find max height to guarantee
        maxH = height[0]
        maxIdx = 0
        for i in range(n):
            if height[i] > maxH:
                maxH = height[i]
                maxIdx = i

        # Move from left to maxIdx
        result = 0
        lpt = 0  # i moves forward (l as left wall)
        for i in range(0, maxIdx):
            if height[i] < height[lpt]:
                result += (height[lpt] - height[i])*1
            else:
                lpt = i
        # Move from right to maxIdx traverse
        r = n - 1  # right wall
        for i in range(n-1, maxIdx, -1):
            if height[i] < height[r]:
                result += height[r] - height[i]
            else:
                r = i
        return result

    def _trap(self, height: List[int]) -> int:
        '''1 Pass: 2 Pairs of Pointers'''
        n = len(height)
        lw = 0  # height of left wall
        lpt = 0
        rpt = n-1
        rw = 0  # will naturall be taken care of
        result = 0
        while lpt <= rpt:
            # which side to process
            if lw <= rw:
                # process left side
                if height[lpt] < lw:
                    result += lw - height[lpt]
                else:
                    lw = height[lpt]
                lpt += 1
            else:
                if height[rpt] < rw:
                    result += rw - height[rpt]
                else:
                    rw = height[rpt]
                rpt -= 1

        return result

    def trap(self, height: List[int]) -> int:
        '''Monotonically Decreasing Stack Solution'''
        res = 0
        n = len(height)
        st = []
        st.append(-1)
        for i in range(n):
            # resolve the stack
            # height at i greater= to top of stack height
            while st[-1] != -1 and height[i] >= height[st[-1]]:
                poppedIdx = st.pop()
                w = i - st[-1] - 1
                # height 0 if using left border
                h = 0
                if st[-1] != -1:
                    h = min(height[i], height[st[-1]]) - height[poppedIdx]
                res += h*w
            st.append(i)

        return res
