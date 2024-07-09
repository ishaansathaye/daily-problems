from typing import List

# LC solution:


def findPairs(self, nums: List[int], k: int) -> int:
    n = len(nums)
    sMap = {}
    count = 0
    # get counts of all numbers
    for i in range(n):
        if nums[i] in sMap:
            sMap[nums[i]] = sMap[nums[i]] + 1
        else:
            sMap[nums[i]] = 1
    # go through keys
    for i in sMap.keys():
        # 0 case: check for counts > 1
        if k == 0 and sMap[i] > 1:
            count += 1
        # > 0 case: check for adding into target only
        elif k > 0 and ((i + k) in sMap):
            count += 1
    return count


# s30 solution:
def findPairs2(nums, k):
    n = len(nums)
    sMap = {}
    sSet = set()
    count = 0
    # get value and idx into hasmap (overwriting dups)
    for i in range(n):
        sMap[nums[i]] = i
    # 0 case: just look for if idx do not match
    if k == 0:
        for i in range(n):
            if nums[i] in sMap and sMap[nums[i]] != i:
                # checking if pair already exists
                if not checkPair(nums[i], nums[i], sSet):
                    count += 1
                    sSet.add((nums[i], nums[i]))
    else:
        # > 0 case: check both values of abs value
        comp = 0
        for num in nums:
            if num - k in sMap or num + k in sMap:
                if num - k in sMap:
                    comp = num - k
                elif num + k in sMap:
                    comp = num + k
                if not checkPair(num, comp, sSet):
                    count += 1
                    sSet.add((num, comp))
    return count


def checkPair(x, y, sSet):
    if (x, y) in sSet or (y, x) in sSet:
        return True
    return False


print(findPairs2([3, 1, 4, 1, 5], 2))
