from typing import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m-1  # start p1 at last element in nums1
    p2 = n-1  # start p2 at last element in nums2
    idx = m+n-1  # start idx at last space in nums1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[idx] = nums1[p1]  # swap 0 with the num1 big element
            p1 -= 1  # decrease both num1 pointers
            idx -= 1
        else:
            nums1[idx] = nums2[p2]  # overwrite nums1 to be nums2 element
            p2 -= 1
            idx -= 1
    while p2 >= 0:  # p1 finishes first but p2 has not finished
        # copy elements of second arr to first one
        nums1[idx] = nums2[p2]
        p2 -= 1
        idx -= 1
