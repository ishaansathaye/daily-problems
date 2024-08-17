def matchingStrings(stringList, queries):
    # Write your code here
    sMap = {}
    for s in queries:
        sMap[s] = 0

    for s in stringList:
        if s in sMap:
            sMap[s] += 1

    res = []
    for s in queries:
        res.append(sMap[s])

    return res
