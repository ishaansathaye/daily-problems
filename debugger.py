def check_2_arrangement(s1, s2):
    counter = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            counter += 1
    if counter > 1 or counter == 0:
        return False
    return True

def chained(inputArray):
    for i in range(len(inputArray)-1):
        if not check_2_arrangement(inputArray[i], inputArray[i+1]):
            return False
    return True


def solution(inputArray):
    # inputArray.sort()
    # newArray = sorted(inputArray)
    # print(inputArray)
    start = 0
    for i in range(len(inputArray)-1):
        truth_values = []
        for j in range(start, len(inputArray)):
            consecutive = check_2_arrangement(inputArray[i], inputArray[j])
            truth_values.append(consecutive)
            if consecutive:
                inputArray[i+1], inputArray[j] = inputArray[j], inputArray[i+1]
                start = i+1
                break
            else:
                inputArray[i], inputArray[j] = inputArray[j], inputArray[i]
        if True not in truth_values:
            return False
    print(inputArray)
    return chained(inputArray)

print()
# print(solution(["aa", "ab", "bb"])) #True
# print(solution(["aba", "bbb", "bab"])) #False
print(solution(["ab", "bb", "aa"])) #True 
# print(solution(["q", "q"])) #False
# print(solution(["abc", "bef", "bcc", "bec", "bbc", "bdc"])) #True -> ["abc", "bbc", "bdc", "bcc", "bec", "bef"]

# print(solution(["ff", "gf", "af", "ar", "hf"])) #True

# print(solution(["ab", "ad", "ef", "eg"])) #False
# print(solution(["abc", "abx", "axx", "abc"])) #False

# print(solution(["abc", "abx", "axx", "abx", "abc"])) #True
print()