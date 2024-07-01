from typing import List

def findMaxLength(self, nums: List[int]) -> int:
    # integer integer hashmap for java
    map = {}
    map.put(0, -1) # running sum of 0 at index -1, this is for the edge case of the initial sub array not being caught
    rSum = 0
    max = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            rSum =- 1
        else:
            rSum += 1
        if map.containsKey(rSum):
            max = max(max, i - map.get(rSum)) # differnce between latest found running sum and first occurence
        else:
            map.put(rSum, i)
    return max