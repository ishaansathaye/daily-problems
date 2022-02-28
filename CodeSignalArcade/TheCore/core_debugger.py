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

print(solution(5,2)) #9
print(solution(15, 5)) #18
print(solution(14, 3)) #20
print(solution(12, 2)) #23