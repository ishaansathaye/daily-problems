from typing import List


class Solution:
    def _canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''Brute Force'''
        minIndex = -1
        n = len(gas)
        for i, pump in enumerate(gas):
            capacity = pump
            j = i
            while capacity > 0:
                capacity -= cost[j]
                if capacity < 0:
                    break
                j += 1
                if j >= n:
                    j = 0
                if j == i:
                    if minIndex == -1:
                        minIndex = i
                    else:
                        minIndex = min(minIndex, i)
                    break
                capacity += gas[j]
        return minIndex

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''Greedy Solution'''
        n = len(gas)
        total_surplus = 0
        current_surplus = 0
        start_index = 0

        for i in range(n):
            petrol, distance = gas[i], cost[i]
            total_surplus += petrol - distance
            current_surplus += petrol - distance

            # If current surplus is negative, reset start index
            if current_surplus < 0:
                start_index = i + 1
                current_surplus = 0

        # If total surplus is non-negative, return start index, else -1
        if total_surplus >= 0:
            return start_index
        return -1
