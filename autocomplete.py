def autocomplete(query_String, set_Strings):
    string_len = len(query_String)
    solution = []
    for item in set_Strings:
        if item[0:string_len] == query_String:
            solution.append(item)
    return solution

queryString = 'de'
setStrings = ['dog', 'deer', 'deal']

print(autocomplete(queryString, setStrings))
