import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''BFS'''
        res = []
        hSet = set()
        q = deque()
        q.append(s)
        hSet.add(s)
        # if valid string at a specific level
        flag = False
        while len(q) != 0 and flag is False:
            size = len(q)
            flag = False
            for i in range(size):
                curr = q.popleft()
                if self.isBalanced(curr):
                    flag = True
                    res.append(curr)
                # put children if not a sol
                if not flag:
                    for k in range(len(curr)):
                        if curr[k].isalnum():
                            continue
                        # remove the kth character
                        child = curr[0:k] + curr[k+1:]
                        if child not in hSet:
                            q.append(child)
                            hSet.add(child)

        return res

    def isBalanced(self, s):
        count = 0
        for i in range(len(s)):
            ch = s[i]
            if ch.isalnum():
                continue
            if ch == '(':
                count += 1
            else:
                # if count is 0 and encountered closing
                # return False
                if count == 0:
                    return False
                count -= 1
        return count == 0

    def _removeInvalidParentheses(self, s: str) -> List[str]:
        '''DFS'''
        self.res = []
        self.hSet = set()
        self.max = 0
        self.dfs(s)
        return self.res

    def dfs(self, s):
        # base
        if len(s) < self.max or s in self.hSet:
            return
        if self.isBalanced(s):
            # only add to res if length of s is greater
            if len(s) > self.max:
                self.max = len(s)
                self.res = []
            self.res.append(s)
        # logic
        self.hSet.add(s)
        for i in range(len(s)):
            if s[i].isalnum():
                continue
            child = s[0:i] + s[i+1:]
            self.dfs(child)
