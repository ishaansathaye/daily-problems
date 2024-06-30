def isIsomorphic(self, s: str, t: str) -> bool:
    # null check
    if len(s) != len(t): # do not need this beacuse len equal
        return False
    #HashMap<CHaracter, CHaracter>
    #sMap = {}
    #2nd HashMap
    #tMap = {}
    # actual solution is making a char array of 100 spots
    for i in range(0, len(s)): # O(n)
        sChar = s[i]
        tChar = t[i]
        if sMap.contains(sChar): # O(1) for everything like this
            if sMap.get(sChar) != tChar:
                return false
            else:
                sMap.put(sChar, tChar)

        if tMap.contains(tChar):
            if tMap.get(tChar) != sCHar:
                return false
            else:
                tMap.put(tChar, sChar)


        if sMap[sChar - ' '] == 0:# 32
            if sMap[sChar - ' '] != tChar:
                return False
            else:
                sMap[sChar - ' '] = tChar

        # do the same for the tMap

    return True

# Solution using 1 HashMap and 1 HashSet
def isIsomorphic(self, s: str, t: str) -> bool:
    # null check
    if len(s) != len(t): # do not need this beacuse len equal
        return False
    #HashMap<CHaracter, CHaracter>
    sMap = {}
    #HashSet<Character> tSet = new HashSet<>();
    tMap = {}
    for i in range(0, len(s)):
        sChar = s.charAt(i)
        tChar = t.charAt(i)
        if sMap.containsKey(sChar):
            if sMap.get(sChar) != tChar:
                return False
        else:
            if tSet.contains(tChar):
                return False
            else:
                sMap.put(sChar, tChar)
                tSet.add(tChar)

    return True


