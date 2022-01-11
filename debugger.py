def alt_solution_help(inputArray):
    for i in range(len(inputArray)):
        if isChainPossible(i, inputArray):
            return True
    return False

def isChainPossible(start, inputArray):
    if len(inputArray) == 1:
        return True
    newArray = inputArray[:start] + inputArray[(1 + start):]
    for i in range(len(newArray)):
        if differsByOne(inputArray[start], newArray[i]) and isChainPossible(i, newArray):
            return True
    return False

def differsByOne(s1, s2):
    if len(s1) != len(s2):
        return False
    differentChars = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differentChars += 1
    return differentChars == 1

print()
print(alt_solution_help(["aa", "ab", "bb"])) #True
print(alt_solution_help(["aba", "bbb", "bab"])) #False
print(alt_solution_help(["ab", "bb", "aa"])) #True 
print(alt_solution_help(["q", "q"])) #False
print(alt_solution_help(["abc", "bef", "bcc", "bec", "bbc", "bdc"])) #True -> ["abc", "bbc", "bdc", "bcc", "bec", "bef"]
print(alt_solution_help(["ff", "gf", "af", "ar", "hf"])) #True
print(alt_solution_help(["ab", "ad", "ef", "eg"])) #False
print(alt_solution_help(["abc", "abx", "axx", "abc"])) #False
print(alt_solution_help(["abc", "abx", "axx", "abx", "abc"])) #True
print()