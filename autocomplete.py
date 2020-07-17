# Problem: Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix. For example, given the query string de and the 
# set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

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
