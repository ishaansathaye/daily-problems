from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        '''O(log(min(n1, n2))) -> BS on smaller list'''
        # null check
        # 1 should always be smaller
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n1 = len(nums1)
        n2 = len(nums2)
        low = 0
        high = n1  # +1 for partitions

        while low <= high:
            partX = low + (high - low) // 2  # middle
            partY = ((n1+n2) // 2) - partX

            # check if good partition
            # get l1, l2, r1, r2
            if partX == 0:
                l1 = -2**31
            else:
                # l1 is on left of partition (1-1) -> first elem
                l1 = nums1[partX-1]

            if partY == 0:
                l2 = -2**31
            else:
                l2 = nums2[partY-1]

            if partX == n1:
                r1 = 2**31
            else:
                r1 = nums1[partX]

            if partY == n2:
                r2 = 2**31
            else:
                r2 = nums2[partY]

            # means correct partition
            # cross comparison
            if l1 <= r2 and l2 <= r1:
                # find median
                if ((n1+n2) % 2) == 0:
                    # even elements
                    return (min(r1, r2) + max(l1, l2)) / 2
                else:
                    # odd elements
                    return min(r1, r2)
            elif l1 > r2:
                high = partX - 1
            else:
                low = partX + 1

    # Binary Search Implementation - 117 ms
    def _findMedianSortedArrays(self, nums1: List[int],
                                nums2: List[int]) -> float:
        f_list = nums1 + nums2
        even = False
        if len(f_list) % 2 == 0:
            target = len(f_list) // 2
            even = True
        else:
            target = len(f_list) // 2

        num_elements = 0
        i = -1
        j = -1
        if len(nums1) == 0:
            current = nums2[0]
            j += 1
        elif len(nums2) == 0:
            current = nums1[0]
            i += 1
        elif nums1[0] < nums2[0]:
            current = nums1[0]
            i += 1
        else:
            current = nums2[0]
            j += 1
        prev = current
        first_pass = False
        sec_pass = False

        while num_elements != target:

            if i+1 <= len(nums1)-1:
                diff1 = nums1[i+1] - current
                first_pass = True
            if j+1 <= len(nums2)-1:
                diff2 = nums2[j+1] - current
                sec_pass = True

            if first_pass and sec_pass:
                if diff1 < diff2:
                    prev = current
                    current = nums1[i+1]
                    i += 1
                else:
                    prev = current
                    current = nums2[j+1]
                    j += 1
            elif first_pass:
                prev = current
                current = nums1[i+1]
                i += 1
            elif sec_pass:
                prev = current
                current = nums2[j+1]
                j += 1

            num_elements += 1
            first_pass = False
            sec_pass = False
        if even:
            return (prev+current)/2
        else:
            return current

    # 252 ms - uses recursion, O(log(m+n)) if use
    # indices instead of list splicing
    def __findMedianSortedArrays(self, A, B):
        lt = 0
        lt = len(A) + len(B)
        if lt % 2 == 1:
            return self.kth(A, B, lt // 2)
        else:
            return (self.kth(A, B, lt // 2) + self.kth(A, B, lt // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's,
            # b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's,
            # a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

    # Original Inefficient - 337 ms
    def ___findMedianSortedArrays2(self, nums1: List[int],
                                   nums2: List[int]) -> float:
        heap = MinHeap()
        conn_list = nums1+nums2
        heap.heap_sort(conn_list)
        mid = len(conn_list)//2
        if len(conn_list) % 2 == 0:
            return (conn_list[mid]+conn_list[mid-1])/2
        return conn_list[mid]


class MinHeap:
    def __init__(self) -> None:
        self.capacity = 0
        self.list_items = [0]
        self.size = 0

    def dequeue(self):
        if self.size == 0:
            return None
        root = self.list_items[1]
        self.list_items[1] = self.list_items[self.size]
        self.size -= 1
        self.list_items.pop()
        self.perc_down(1)
        return root

    def build_heap(self, alist):
        self.list_items = [0]
        if self.capacity < len(alist):
            self.capacity = len(alist)
        self.list_items += alist
        self.size = len(alist)
        initial_parent = len(alist)//2
        while initial_parent > 0:
            self.perc_down(initial_parent)
            initial_parent -= 1

    def perc_down(self, i):
        while 2*i <= self.size:
            if 2*i+1 > self.size:
                min_index = 2*i
            else:
                if self.list_items[2*i] < self.list_items[(2*i)+1]:
                    min_index = 2*i
                else:
                    min_index = (2*i)+1
            if self.list_items[i] > self.list_items[min_index]:
                self.list_items[i],
                self.list_items[min_index] = self.list_items[min_index],
                self.list_items[i]
            i = min_index

    def heap_sort(self, alist):
        self.build_heap(alist)
        for i in range(len(alist)):
            alist[i] = self.dequeue()


temp = Solution()
# print(temp.findMedianSortedArrays(nums1=[1,2], nums2=[3,4])) #2.5
# print(temp.findMedianSortedArrays(nums1=[1,3], nums2=[2])) #2
# print(temp.findMedianSortedArrays(nums1=[], nums2=[1])) #1
# print(temp.findMedianSortedArrays(nums1=[1,3], nums2=[2,7])) #2.5
print(temp.findMedianSortedArrays(nums1=[], nums2=[2, 3]))  # 2.5
