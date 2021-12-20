def solution2(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return solution2(s[:start] + s[start+1:end][::-1] + s[end+1:]) #uses recursion
    return s
print(solution2(s="foo(bar(baz))blim"))