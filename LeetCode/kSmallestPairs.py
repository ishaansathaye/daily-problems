from typing import List
from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int],
                       k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)

        res = []
        pq = []
        visited = set()
        heappush(pq, (nums1[0]+nums2[0], 0, 0))

        while k > 0 and pq:
            _, idx1, idx2 = heappop(pq)
            # append the min sum numbers in the heap
            res.append([nums1[idx1], nums2[idx2]])

            # add both combinations of the previous sum's indices
            # i+1, j and i, j+1
            if idx1+1 < m and (idx1+1, idx2) not in visited:
                heappush(pq, (nums1[idx1+1]+nums2[idx2], idx1+1, idx2))
                visited.add((idx1+1, idx2))
            if idx2+1 < n and (idx1, idx2+1) not in visited:
                heappush(pq, (nums1[idx1]+nums2[idx2+1], idx1, idx2+1))
                visited.add((idx1, idx2+1))

            k -= 1

        return res


if __name__ == "__main__":
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    s = Solution()
    print(s.kSmallestPairs(nums1, nums2, k))
