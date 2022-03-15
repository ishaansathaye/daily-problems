class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #92 ms
        int_dict = {}
        for i in range(len(nums)):
            int_dict[str(nums[i])] = (target-nums[i], i)
        for i in range(len(nums)):
            if str(target-nums[i]) in int_dict and i != int_dict[str(target-nums[i])][1]:
                return [i, int_dict[str(target-nums[i])][1]]

    #Two-Pass Hash Table
    def twoSumAlternate(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    #One-Pass Hash Table
    def twoSumAlternate(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

    #Using enumerate
    def twoSumAlternate(self, nums, target):
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx

        #O(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i]+nums[j] == target:
        #             return [i, j]

temp = Solution()
print(temp.twoSum([2,7,11,15], 9))
print(temp.twoSum([3,3], 6))
print(temp.twoSum([3,2,4], 6))
print(temp.twoSum([-1, -2, -3, 4], 2))