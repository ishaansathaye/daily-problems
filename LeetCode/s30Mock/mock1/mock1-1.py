def findMissing(nums, n):
    # null case
    
    if (len(nums) == 0):
        return None
    if nums[0] != 1:
        return 1
    if (len(nums)+1) != nums[len(nums)-1]:
        return n
    l = 0
    h = len(nums)-1
    while (l <= h):
        m = (h + l) // 2
        if (m > 0 and nums[m]-1 != nums[m-1]):
            return nums[m]-1
        elif (m != len(nums)-1 and nums[m]+1 != nums[m+1]):
            return nums[m]+1
        if (nums[m]-1) != m:
            h = m - 1
        else:
            l = m + 1

arr = [1,2,3,4,5,6,8]
arr2 = [2,3,4,5,6,7,8]
arr3 = [1,2,3,4,5,6,7]
arr4 = [1,3,4,5,6,7,8]
print(findMissing(arr4, 8))
