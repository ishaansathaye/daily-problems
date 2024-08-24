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

    def strStr1(self, haystack: str, needle: str) -> int:
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

    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        lps = self.lps(needle)
        i = 0  # haystack pointer
        j = 0  # needle pointer
        while i < m:
            if haystack[i] == needle[j]:
                # continue - go to next
                i += 1
                j += 1
                # reached end of needle
                if j == n:
                    # return the start index of where
                    # i stopped - length of needle
                    return i - n
            elif haystack[i] != needle[j] and j > 0:
                # mismatch
                # make use of longest common prefix and suffix at previous char
                j = lps[j - 1]
            elif haystack[i] != needle[j] and j == 0:
                # very first characters not matching
                i += 1
        return -1

    def lps(self, needle):
        lps = [0 for _ in range(len(needle))]
        i = 1
        j = 0  # keeping track of prefix
        while i < len(lps):
            # case 1
            # if incoming prefix = suffix
            if needle[j] == needle[i]:
                # increase length of prefix window
                j += 1
                lps[i] = j  # prefix length
                i += 1
            elif needle[j] != needle[i] and j > 0:
                # squeeze the window
                # no need to check in between things
                j = lps[j-1]
            elif needle[j] != needle[i] and j == 0:
                lps[i] = j  # 0 lps[i] = 0
                i += 1
        return lps
