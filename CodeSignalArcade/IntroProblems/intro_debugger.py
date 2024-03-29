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

def solution(s):
    s_list = list(s)
    indices = []
    prev = ""
    for i in range(len(s)):
        if prev != s[i] and prev != "":
            indices.append(i)
        prev = s[i]
    offset = 0
    for i in indices:
        s_list.insert(i+offset, " ")
        offset += 1
    s_list = "".join(s_list)
    s_list = s_list.split(" ")
    for i in range(len(s_list)):
        if len(s_list[i]) > 1:
            s_list[i] = str(len(s_list[i])) + s_list[i][0]
    return "".join(s_list)
    
# print(solution("aabbbc"))
# print(solution("abbcabb"))

def solution(text):
    new_text = list(text)
    for i in range(len(new_text)):
        if not new_text[i].isalpha():
            new_text[i] = " "
    new_text = "".join(new_text)
    text = new_text.split(" ")
    text = [i for i in text if i != ""]
    lengths_list = [len(i) for i in text]
    return text[lengths_list.index(max(lengths_list))]
    

# print(solution("Ready, steady, go!"))
# print(solution("ABCd"))
# print(solution("To be or not to be"))

def solution(p):
    if p == 0: return 10
    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == p: return i
    return -1

# print(solution(12))

def solution(p):
    if p == 0:
        return 10
    elif p == 1:
        return 1
    n = []
    while 1 < p:
        for d in range(9, 1, -1):
            if p % d == 0:
                p /= d
                n.append(d)
                break
        else:
            return -1
    return int(''.join(map(str, sorted(n))))

# print(solution(12))
# print(solution(19))
# print(solution(600))
# print(solution(450))

def solution(names):
    temp = []
    for i in range(len(names)):
        k = 1
        old = names[i]
        if names[i] not in temp:
            temp.append(names[i])
        else:
            while names[i] in temp:
                names[i] = old + "(" + str(k) + ")"
                k += 1
        if names[i] not in temp:
            temp.append(names[i])
    return names

# print(solution(["doc", "doc", "image", "doc(1)", "doc"]))
# print(solution(["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]))
# print('["a(1)", "a(6)", "a", "a(2)", "a(3)", "a(4)", "a(5)", "a(7)", "a(8)", "a(9)", "a(10)", "a(11)"]')
# print(["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"])
# print(solution(["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]))
# print(["dd", "dd(1)", "dd(2)", "dd(3)", "dd(1)(1)", "dd(1)(2)", "dd(1)(1)(1)", "dd(4)", "dd(1)(3)"])

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    
def solution(n):
    matrix = []
    temp = []
    for i in range(n):
        for j in range(n):
            temp.append('-')
        matrix.append(temp)
        temp = []

    row, col = 0, 0
    row_step, col_step = 1, 1
    stop = n
    iterator = 'c'
    counter = 0
    for z in range(0, (n*2)-1):
        if iterator == 'c':
            for i in range(col, stop, col_step):
                if matrix[row][i] != '-':
                    break
                counter += 1
                matrix[row][i] = counter
                previous = i
            iterator = 'r'
            col = previous
            if row >= n-1 or matrix[row+1][col] != '-':
                row -= 1
                stop = -1
                row_step = -1
            else:
                row += 1
                stop = n
                row_step = 1
        else:
            for i in range(row, stop, row_step):
                if matrix[i][col] != '-':
                    break
                counter += 1
                matrix[i][col] = counter
                previous = i
            iterator = 'c'
            row = previous
            if col >= n-1 or matrix[row][col+1] != '-':
                col -= 1
                stop = -1
                col_step = -1
            else:
                col += 1
                stop = n
                col_step = 1
    return matrix

# print(solution(3))
# print_matrix(solution(2))

def solution(grid):
    checks = []
    numbers = [i for i in range(1, 10)]
    for row in range(len(grid)):
        print(grid[row])
        if not all(item in numbers for item in grid[row]):
            checks.append(0)
    
    for col in range(len(grid[0])):
        temp_col = []
        for row in range(len(grid)):
            temp_col.append(grid[row][col])
        if not all(item in temp_col for item in numbers):
            checks.append(0)
            break
    
    grid_3 = []
    for row in range(1):
        for col in range(0, 1):
            grid_3 += [grid[row][col], grid[row][col+1], grid[row][col+2]]
            grid_3 += [grid[row+1][col], grid[row+1][col+1], grid[row+1][col+2]]
            grid_3 += [grid[row+2][col], grid[row+2][col+1], grid[row+2][col+2]]
        if not all(item in grid_3 for item in numbers):
            checks.append(0)
            break
        
    return sum(checks) == []

# print(solution(
# [[1,3,2,5,4,6,9,2,7], 
#  [4,6,5,8,7,9,3,8,1], 
#  [7,9,8,2,1,3,6,5,4], 
#  [9,2,1,4,3,5,8,7,6], 
#  [3,5,4,7,6,8,2,1,9], 
#  [6,8,7,1,9,2,5,4,3], 
#  [5,7,6,9,8,1,4,3,2], 
#  [2,4,3,6,5,7,1,9,8], 
#  [8,1,9,3,2,4,7,6,5]]))