# exhaustive approach
def maxArea(self, height: List[int]) -> int:
    max  = Integer.MIN_Value
    n = len(height)
    for i in range(n):
        for j in range(i+1, n):
            currArr = min(height[i], height[j]) * (j - i) # smaller height becomes height of area and width is diff of indices
            max = max(max, currArr)
    return max

def maxArea(self, height: List[int]) -> int: # O(n) and O(1)
    l = 0
    r = n - 1
    while (l < r):
        currAr = min(height[l], height[r]) * (r - l)
        max = max(max, currAr)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return max
