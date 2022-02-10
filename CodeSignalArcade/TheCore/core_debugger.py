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
print(solution(2,2,1,2))