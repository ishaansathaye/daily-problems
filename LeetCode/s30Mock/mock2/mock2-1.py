from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    sMap = {}
    for i in range(0, len(nums)):
        if nums[i] not in sMap.keys():
            sMap[nums[i]] = i
        y = target - nums[i]
        if y in sMap.keys():
            if i != sMap[y]:
                return [sMap[y], i]
