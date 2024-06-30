def wordPattern(pattern: str, s: str) -> bool:
    p = {}
    sSet = set()
    source = s.split(" ")
    if len(pattern) != len(source):
        return False
    for i in range(len(pattern)):
        if pattern[i] in p.keys():
            if p[pattern[i]] != source[i]:
                return False
        else:
            if source[i] in sSet:
                return False
            p[pattern[i]] = source[i]
            sSet.add(source[i])
    return True


#s = "dog cat cat fish"
s2 = "dog dog dog dog"
pattern = "abba"
print(wordPattern(pattern, s2))

