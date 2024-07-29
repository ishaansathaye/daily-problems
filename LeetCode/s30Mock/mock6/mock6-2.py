class Solution:
    count = 0
    hSet = set()

    def countArrangement(self, n: int) -> int:
        self.helper(n)
        return self.count

    def helper(self, n):
        '''Do not need to keep track of path'''
        '''O(n!)'''
        # base
        if len(self.hSet) == n:
            self.count += 1
            return
        # logic
        for i in range(1, n+1):
            # do not want to add duplicates:
            if i in self.hSet:
                continue
            # add to set
            self.hSet.add(i)
            # check before recursing -> optimization
            if len(self.hSet) % i == 0 or i % len(self.hSet) == 0:
                self.helper(n)
            # backtrack
            self.hSet.remove(i)
