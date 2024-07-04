from typing import List


def exhaustiveMaxArea(self, height: List[int]) -> int:
    '''Exhaustive Approach'''
    max_val = -2**31  # smallest value an int can have
    n = len(height)
    for i in range(n):
        for j in range(i+1, n):
            # smaller height becomes height of area
            # and width is diff of indices
            currAr = min(height[i], height[j]) * (j - i)
            max_val = max(max_val, currAr)
    return max_val


def maxArea(self, height: List[int]) -> int:  # O(n) and O(1)
    '''Tow Pointers Approach'''
    n = len(height)
    left = 0
    right = n - 1
    max_val = -2**31
    while (left < right):
        currAr = min(height[left], height[right]) * (right - left)
        max_val = max(max_val, currAr)
        if height[left] <= height[right]:  # move the lesser pointer value
            left += 1
        else:
            right -= 1
    return max_val
