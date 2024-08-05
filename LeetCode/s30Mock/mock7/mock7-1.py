from typing import List
from heapq import heappush, heappop


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        for t in intervals:
            # seeing if end time in pq is greater than
            # next start time (overlap)
            if len(pq) == 0 or pq[0] > t[0]:
                # new meeting room
                heappush(pq, t[1])
            else:
                # no new meeting room (evict)
                heappop(pq)
                heappush(pq, t[1])
        return len(pq)
