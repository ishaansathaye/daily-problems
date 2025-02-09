class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if s == "":
            return True
        sptr = 0
        tptr = 0
        for tptr in range(len(t)):
            if s[sptr] == t[tptr]:
                sptr += 1
            if sptr == len(s):
                return True
        return False
