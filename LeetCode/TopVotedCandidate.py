from typing import List
from collections import defaultdict


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.countMap = defaultdict(int)
        self.leadersMap = defaultdict(int)
        leader = 0
        for i in range(len(persons)):
            currTime = times[i]
            currPerson = persons[i]
            self.leadersMap[currPerson] += 1
            if self.leadersMap[currPerson] >= self.leadersMap[leader]:
                leader = currPerson
            self.countMap[currTime] = leader

    def q(self, t: int) -> int:
        if t in self.countMap:
            return self.countMap[t]
        # binary search on time arr
        low = 0
        high = len(self.times)-1
        while low <= high:
            mid = low + (high - low) // 2
            if self.times[mid] > t:
                high = mid - 1
            else:
                low = mid + 1
        # since cross: high at lower value
        return self.countMap[self.times[high]]

    # Solution #2: fill all times until next timestamp

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
