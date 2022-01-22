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

# print()
# print(alt_solution_help(["aa", "ab", "bb"])) #True
# print(alt_solution_help(["aba", "bbb", "bab"])) #False
# print(alt_solution_help(["ab", "bb", "aa"])) #True 
# print(alt_solution_help(["q", "q"])) #False
# print(alt_solution_help(["abc", "bef", "bcc", "bec", "bbc", "bdc"])) #True -> ["abc", "bbc", "bdc", "bcc", "bec", "bef"]
# print(alt_solution_help(["ff", "gf", "af", "ar", "hf"])) #True
# print(alt_solution_help(["ab", "ad", "ef", "eg"])) #False
# print(alt_solution_help(["abc", "abx", "axx", "abc"])) #False
# print(alt_solution_help(["abc", "abx", "axx", "abx", "abc"])) #True
# print()

from itertools import permutations as p
def solution(inputArray):
    for ia in p(inputArray):
        c = 0
        for i in range(len(ia) - 1):
            for j in range(len(ia[i])):
                if ia[i][j] != ia[i+1][j]: c += 1
            if ia[i] == ia[i+1]: c += 10
        if c == len(ia) - 1: return True
    return False

# print(solution(["aa", "ab", "bb"])) #True
# print(solution(["aba", "bbb", "bab"])) #False
# print(solution(["ab", "bb", "aa"])) #True 
# print(solution(["q", "q"])) #False
# print(solution(["abc", "bef", "bcc", "bec", "bbc", "bdc"])) #True -> ["abc", "bbc", "bdc", "bcc", "bec", "bef"]
# print(solution(["ff", "gf", "af", "ar", "hf"])) #True
# print(solution(["ab", "ad", "ef", "eg"])) #False
# print(solution(["abc", "abx", "axx", "abc"])) #False
# print(solution(["abc", "abx", "axx", "abx", "abc"])) #True

def solution(n, counter=0):
    if len(str(n)) == 1:
        return 0
    counter = solution(sum([int(i) for i in str(n)]), counter) + 1
    return counter

# print(solution(91))

def solution(s):
    if s.count('-') == 5:
        s_list = s.split('-')
        for i in s_list:
            if len(i) != 2:
                return False
        s_list = "".join(s_list)
        for i in s_list:
            if i.isdigit():
                if int(i) < 0 or int(i) > 9:
                    return False
            elif i.isalpha():
                if ord(i) < 65 or ord(i) > 70:
                    return False
        return True

# print(solution("00-1B-63-84-45-E6"))
# print(solution("Z1-1B-63-84-45-E6"))
