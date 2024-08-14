from typing import List


class Solution:
    def __wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''Brute Force (tree on every letter)'''
        hSet = set(wordDict)  # trie in production
        # self.flag = False
        return self.helper(s, hSet)
        # return self.flag

    # can do with pivot or this way with substring
    def __helper(self, s, hSet):
        # base
        if len(s) == 0:
            return True

        # logic
        for i in range(len(s)):
            # action
            curr = s[0:i+1]
            # if substring in set and rest in set
            if curr in hSet and self.helper(s[i+1:], hSet):
                return True
        return False

    def _wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''Top-Down DP ~ N^3'''
        hSet = set(wordDict)
        memoMap = {}
        return self.helper(s, hSet, memoMap)

    def helper(self, s, hSet, memoMap):
        # base
        if len(s) == 0:
            return True
        if s in memoMap:
            return memoMap[s]

        # logic
        for i in range(len(s)):
            # action
            curr = s[0:i+1]
            if curr in hSet:
                restStringResult = self.helper(s[i+1:], hSet, memoMap)
                if restStringResult:
                    memoMap[s] = restStringResult
                    return True

        memoMap[s] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''Bottom-Up DP'''
        hSet = set(wordDict)  # O(N*l)
        le = len(s)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True  # empty string before is splittable
        for i in range(1, len(dp)):
            for j in range(0, i):
                if dp[j] and s[j:i] in hSet:
                    dp[i] = True
                    break
        return dp[le]
