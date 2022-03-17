from typing import List
class Solution:
    #Binary Search Implementation
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass
    
    #Inefficient
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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
                    self.list_items[i], self.list_items[min_index] = self.list_items[min_index], self.list_items[i]
                i = min_index
        
        def heap_sort(self, alist):
            self.build_heap(alist)
            for i in range(len(alist)):
                alist[i] = self.dequeue()

temp = Solution()
# print(temp.findMedianSortedArrays(nums1=[1,2], nums2=[3,4])) #2.5
print(temp.findMedianSortedArrays(nums1=[1,3], nums2=[2])) #2
        