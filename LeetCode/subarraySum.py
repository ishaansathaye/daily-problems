from typing import List

def subarraySum(self, nums: List[int], k: int) -> int:
    map = {}
    map.put(0, 1) # dummy entry that 0 sum has happenend once to take care of first subarray
    count = 0
    rSum = 0
    for i in range(0, len(nums)):
        rSum += nums[i]
        #y = x - z
        if map.containsKey(rSum - k): # if that target has happened before
            count += map.get(rSum - k)
        if !map.containsKey(rSum):
            map.put(rSum, 1)
        else:
            map.put(rSum, map.get(rSum)+1)
    return count
