from collections import defaultdict, deque


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        '''Greedy Solution: Target -> Start'''
        '''log(n)'''
        count = 0
        while target > startValue:
            if target % 2 == 0:
                target = target // 2
            else:
                target += 1
            count += 1
        # if target becomes smaller: 5 -> 8
        return count + startValue - target

    def _brokenCalc(self, startValue: int, target: int) -> int:
        '''BFS -> Memory Limit Exceeded'''
        # number is greater than target -> no need to add to q
        # no need to add if visited
        q = deque()
        q.append(startValue)
        hSet = set()  # for visited
        hSet.add(startValue)
        count = 0
        while len(q) != 0:
            size = len(q)  # each level done then increase count
            for i in range(size):
                curr = q.popleft()
                if curr == target:
                    return count
                if curr < target:
                    child1 = curr*2
                    if child1 not in hSet:
                        hSet.add(child1)
                        q.append(child1)
                if curr > 1:
                    child2 = curr - 1
                    if child2 not in hSet:
                        hSet.add(child2)
                        q.append(child2)
            count += 1
        return count

    def brokenCalc1(self, startValue: int, target: int) -> int:
        '''DFS'''
        self.memo = defaultdict()
        return self.dfs(startValue, target)

    def dfs(self, startValue, target):
        # base
        if startValue < 1:
            self.memo[startValue] = 2**31
            return 2**31
        if startValue >= target:
            self.memo[startValue] = startValue - target
            return startValue - target
        if startValue in self.memo:
            return self.memo[startValue]
        # logic
        # max rec depth exceeded:
        case1 = self.dfs(startValue*2, target)
        case2 = self.dfs(startValue-1, target)
        res = min(case1, case2) + 1
        self.memo[startValue] = res
        return res
