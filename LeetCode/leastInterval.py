from typing import List
from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hMap = defaultdict(int)  # char:int
        maxFreq = 0
        for i in range(len(tasks)):
            task = tasks[i]
            hMap[task] += 1
            # finding maxFreq number
            maxFreq = max(maxFreq, hMap[task])

        # how many with max freq
        maxCount = 0
        for task in hMap.keys():
            if hMap[task] == maxFreq:
                maxCount += 1

        partitions = maxFreq - 1
        # what is the effective n
        # - 1 to calc spots left in partition
        # after maxFreq are put together
        availableSlots = partitions*(n-(maxCount-1))
        # (length - already scheduled tasks) = pending
        pendingTasks = len(tasks) - (maxFreq*maxCount)
        idle = max(0, availableSlots - pendingTasks)

        return len(tasks) + idle
