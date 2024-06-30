def binarySearchFirst(nums, target, low, high): # can do recursive but log(n) space
# because of recursion overhead, in iteration space is O(1) ONLY FOR THIS PROBLEM
    while (low <= high):
        mid = low + (high - low) / 2
        if nums[mid] == target:
            if (mid == 0 or nums[mid] != nums[mid - 1]):
                return mid
            else:
                high = mid - 1 # not the first occurnance so move left
        elif nums[mid] < target:
            # move right
            low = mid + 1
        else:
            # move left
            high = mid - 1

def binarySearchLast(nums, target, low, high): # can do recursive but log(n) space
# because of recursion overhead, in iteration space is O(1) ONLY FOR THIS PROBLEM
    while (low <= high):
        mid = low + (high - low) / 2
        if nums[mid] == target:
            if (mid == (len(nums) - 1) or nums[mid] != nums[mid + 1]):
                return mid
            else:
                low = mid + 1 # not the last occurance so move right
        elif nums[mid] < target:
            # move right
            low = mid + 1
        else:
            # move left
            high = mid - 1




def searchRange(self, nums: List[int], target: int) -> List[int]:
    # null case check 
    first = binarySearchFirst(nums, target, 0, len(nums)-1)
    if first == -1:
        return [-1, -1]
    last = binarySearchLast(nums, target, first, len(nums)-1)
    return [first, last]

