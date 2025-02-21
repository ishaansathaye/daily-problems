from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str,
                    bank: List[str]) -> int:
        # keep track of steps from the current gene as a tuple
        q = deque([(startGene, 0)])
        # visited set
        hSet = set(startGene)

        while len(q) > 0:
            currGene, count = q.popleft()
            if currGene == endGene:
                return count
            count += 1
            # go through all the neigbours of the current gene
            # changing each char in the string
            # checking if visited already or in bank
            # then bfs on those next genes
            for c in "ACGT":
                for i in range(len(currGene)):
                    nextGene = currGene[:i] + c + currGene[i+1:]
                    if nextGene not in hSet and nextGene in bank:
                        q.append((nextGene, count))
                        hSet.add(nextGene)
        return -1


'''
start = a a c c g g t t
end   = a a a c g g t a

bank
a a c c g g t a
a a c c g c t a
a a a c g g t a
'''
