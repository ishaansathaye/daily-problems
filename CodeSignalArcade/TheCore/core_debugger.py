def solution(min1, min2_10, min11, s):
    minutes = 0
    if s-min1 ==  0:
        return 1
    while s > 0:
        if minutes == 0:
            s -= min1
            if s-min1 >= 0:
                minutes = 2
        elif 2 <= minutes <= 10:
            s -= min2_10
            if s-min2_10 >= 0:
                minutes += 1
        elif minutes > 10:
            s -= min11
            if s-min11 >= 0:
                minutes += 1
    return minutes
    

# print(solution(3,1,2,20))
# print(solution(10,1,2,22))
# print(solution(1,2,1,6))
# print(solution(10, 10, 10, 8))
# print(solution(2,2,1,2))

def solution(commands):
    s1=s2=1
    directionsL = [1,2,-1,-2]
    directionsR = [1,-2,-1,2]
    iterator = 0
    same = 0
    for i in commands:
        if i == 'L':
            iterator += 1
            if iterator > 3:
                iterator = 0
            s1 = directionsL[iterator]
            s2 = directionsR[iterator]
        elif i == 'A':
            s1 *= -1
            s2 *= -1
            iterator = directionsR.index(s1)
        elif i == 'R':
            iterator += 1
            if iterator > 3:
                iterator = 0
            s1 = directionsR[iterator]
            s2 = directionsL[iterator]
        if s1 == s2:
            same += 1
    return same

# print(solution("LLARL")) #3

def solution(candlesNumber, makeNew):
    candles = candlesNumber
    leftovers = 0
    while (candlesNumber+leftovers) >= makeNew:
        temp = candlesNumber
        candlesNumber = (candlesNumber+leftovers)//makeNew
        leftovers = (leftovers+temp)%makeNew
        candles += candlesNumber
        if leftovers == 0 and (candlesNumber+leftovers) < makeNew:
            break
    return candles

# print(solution(5,2)) #9
# print(solution(15, 5)) #18
# print(solution(14, 3)) #20
# print(solution(12, 2)) #23

def solution(n):
    list_num = []
    list_num.append(n)
    next_elem = calc_elem(n)
    while True:
        list_num.append(next_elem)
        prev_elem = next_elem
        next_elem = calc_elem(next_elem)
        if next_elem == prev_elem and next_elem != 1:
            list_num.append(next_elem)
            break
        elif next_elem in list_num and next_elem != 1:
            list_num.append(next_elem)
            break
        elif list_num.count(1) == 2:
            break
    return list_num

def calc_elem(n):
    n_length = len(str(n))
    new_n = 0
    for i in range(n_length):
        new_n += (n%10)**2
        n = n//10
    return new_n

# print(solution(16))
# print(solution(103))
# print(solution(1))
# print(solution(612))

def solution(n):
    weak_dict = find_weakness(n)
    max_weakness = max(weak_dict.values())
    return [max_weakness, list(weak_dict.values()).count(max_weakness)]

def find_weakness(x):
    divisors_dict = find_divisors(x)
    weakness = {}
    for i in range(1, x+1):
        weak_count = 0
        for j in range(1, i+1):
            if j < x and divisors_dict[str(j)] > divisors_dict[str(i)]:
                weak_count += 1
        weakness[str(i)] = weak_count
    return weakness

def find_divisors(n):
    divisors = {}
    for i in range(1, n+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        divisors[str(i)] = count
    return divisors

print(solution(9))