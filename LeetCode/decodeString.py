class Solution:
    def __init__(self):
        self.idx = 0

    def decodeString(self, s: str) -> str:
        '''DFS'''
        strSt = []  # in Java this is using String Builder for mutability
        numSt = []
        currNum = 0
        currStr = ""
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                # getting ascii value of c
                currNum = currNum*10 + (ord(c) - ord('0'))
            elif c == '[':
                # add all to stack
                numSt.append(currNum)
                strSt.append(currStr)
                # reset all these
                currNum = 0
                currStr = ""
            elif c == ']':
                # pop the num...get the num corresponding to baby
                count = numSt.pop()
                # separate string for the baby (do not want to use currStr)
                baby = ""
                for k in range(count):
                    baby += currStr
                # combine with parent
                parent = strSt.pop()
                currStr = parent + baby
            else:  # is normal character
                currStr += c
        return currStr  # .toString since it was StringBuilder in Java

    def _decodeString(self, s: str) -> str:
        '''DFS with Recursion'''
        currNum = 0
        currStr = ""
        while self.idx < len(s):
            c = s[self.idx]
            if c.isdigit():
                # getting ascii value of c
                currNum = currNum*10 + (ord(c) - ord('0'))
                self.idx += 1
            elif c == '[':
                # baby has started
                # recursively decode the baby first
                self.idx += 1
                # not breaking because idx is global
                baby = self.decodeString(s)
                # according to count append to parent
                for k in range(currNum):
                    currStr += baby
                currNum = 0
            elif c == ']':
                # base case (null in dfs tree)
                self.idx += 1
                return currStr  # .toString
            else:  # is normal character
                currStr += c
                self.idx += 1
        return currStr
