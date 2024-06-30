# solution with 1 pass
def longestPalindrome(self, s: str) -> int: # O(n)
    # make a hashset in java
    pals = set()
    result = 0
    for i in range(0, len(s)):
        if s[i] in pals:
            result += 2
            pals.remove(s[i])
        else:
            pals.add(s[i])
    if len(pals) != 0:
        return result+1
    else:
        return result

# solution with 2 passes:
def longestPalindrome(self, s: str) -> int:
    pass
