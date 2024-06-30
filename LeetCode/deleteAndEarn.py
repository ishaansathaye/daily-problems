def deleteAndEarn(self, nums: List[int]) -> int:
    int max = INteger.min_value;
    max(nums)
    arr = new int[max+1]
    for i in nums:
        arr[num] += num
    prev = arr[0]
    curr = max(arr[0], arr[1])
    for i in range(2, max+1): # O(m) --> O(max(n))
        temp = curr
        curr = max(curr, prev+nums[i])
        prev = temp
    return curr

