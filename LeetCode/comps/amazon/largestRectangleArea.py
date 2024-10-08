from typing import List
from collections import deque


class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxarea = max(maxarea, height*(i-index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxarea = max(maxarea, h*(len(heights)-i))
        return maxarea

    def _largestRectangleArea(self, heights: List[int]) -> int:
        '''Brute Force'''
        maxArea = 0
        n = len(heights)
        for i in range(n):
            minArea = heights[i]
            for j in range(i, n):
                minArea = min(minArea, heights[j])
                currArea = (j-i+1)*minArea
                maxArea = max(currArea, maxArea)
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        '''Monotonic Stack'''
        maxArea = 0
        n = len(heights)
        st = deque()  # of indices only
        st.append(-1)
        for i in range(n):
            # want a increasing stack
            while st[-1] != -1 and heights[i] < heights[st[-1]]:
                # resolve stack pop
                popped = st.pop()
                # i is the right boundary
                # peek is the left boundary
                currArea = heights[popped]*(i - st[-1] - 1)
                maxArea = max(currArea, maxArea)
            st.append(i)
        # resolve pending elements when i is done
        while st[-1] != -1:
            popped = st.pop()
            currArea = heights[popped]*(n - st[-1]-1)
            maxArea = max(currArea, maxArea)
        return maxArea
