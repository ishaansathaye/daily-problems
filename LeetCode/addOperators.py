from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def addOperators(self, num: str, target: int) -> List[str]:
        '''Without Backtracking (Creating new Strings Everytime)'''
        self.helper(num, 0, "", 0, 0, target)
        return self.res

    def helper(self, num, pivot, path, calc, tail, target):
        # base
        if pivot == len(num):
            if calc == target:
                self.res.append(path)
            return
        # logic
        # creating the level:
        for i in range(pivot, len(num)):
            # preceding zero case
            # only when i is further ahead: "05"
            if num[pivot] == "0" and i != pivot:
                continue
            # ex: 1, 12, 123
            curr = int(num[pivot:i+1])
            if pivot == 0:
                # at the top level
                self.helper(num, i+1, path+str(curr), curr, curr, target)
            else:
                # +
                self.helper(num, i+1, path+"+"+str(curr),
                            calc+curr, curr, target)
                # -
                self.helper(num, i+1, path+"-"+str(curr),
                            calc-curr, -curr, target)
                # *
                self.helper(num, i+1, path+"*"+str(curr), calc -
                            tail+(tail*curr), tail*curr, target)
