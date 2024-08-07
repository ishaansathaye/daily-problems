class Solution:
    def _strStr(self, haystack: str, needle: str) -> int:
        """Brute Force with i and j O(mxn)"""
        i = 0  # pointer at haystack
        m = len(haystack)
        n = len(needle)
        while i <= m - n:  # m-n is the last length possible
            if haystack[i] == needle[0]:
                k = i  # iterating on haystack
                j = 0  # iterating on needle
                while haystack[k] == needle[j]:
                    j += 1
                    k += 1
                    if j == n:
                        return i
            i += 1
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        '''Robin-Karp Algo: O(M+N)'''
        m = len(haystack)
        n = len(needle)

        hashP = 0
        for i in range(n):
            c = needle[i]
            hashP = hashP*26 + ord(c) - ord('a') + 1

        # kl = Math.pow(26, n-1)
        # in notes is 10^(5-1)
        kl = 26**(n-1)
        hashS = 0
        for i in range(m):
            # outgoing character
            if i >= n:
                out = haystack[i-n]
                # subtracting the contribution of outgoing
                hashS = hashS - (ord(out)-ord('a')+1) * kl

            # ingoing character
            inC = haystack[i]
            hashS = hashS*26 + ord(inC) - ord('a') + 1

            if hashS == hashP:
                return i-n+1  # the first pointer

        return -1
