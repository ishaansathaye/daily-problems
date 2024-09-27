from collections import deque


class Solution:
    def __init__(self):
        self.hMap = {
            8: 8,
            6: 9,
            0: 0,
            1: 1,
            9: 6,
        }

    def confusingNumberII(self, n: int) -> int:
        '''DFS'''
        self.count = 0
        self.n = n
        self.dfs(0)
        return self.count

    def dfs(self, curr):
        # base
        if curr > self.n:
            return
        # logic
        if self.isConfusing(curr):
            self.count += 1
        # make new children
        for digit in self.hMap.keys():
            newNum = curr*10 + digit
            if newNum != 0:
                self.dfs(newNum)

    def isConfusing(self, num):
        res = 0
        temp = num
        while temp > 0:
            # get the digit
            digit = temp % 10
            res = res*10 + self.hMap[digit]
            temp = temp // 10

        return num != res

    def _confusingNumberII(self, n: int) -> int:
        '''BFS'''
        q = deque()
        q.append(0)
        self.count = 0
        while len(q) != 0:
            curr = q.popleft()
            if curr > n:
                continue
            if self.isConfusing(curr):
                self.count += 1
            for digit in self.hMap.keys():
                newNum = curr*10 + digit
                if newNum != 0:
                    q.append(newNum)
        return self.count
