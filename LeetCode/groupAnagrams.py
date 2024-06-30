from typing import List

# prime number solution - as boilerplate code 
prime = {2, 3, 5, 7 ...}
primeProduct = primeProduct(s)

def primeProduct(s): # full solution results in O(n*k)
    result = 1
    for i in range(0, len(s)):
        c = s.charAt(i)
        result = result * prime[c-'a'] # that is the ASCII key 
    return result


def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # O(nllogl + l) = O(nllogl)
    # HashMap<String, List<String> map = new HashMap
    map = {} # Space is O(n*l) where n is is length of map and l is the length of each
    for s in strs: # O(n) 
        # sort this s
        # char [] charArr = s.toCharArray()
        sortedStr = sort(s)
        if map.containsKey(sortedStr): #O(llogl)
            map.put(sortedStr, [])
        map.get(sortedStr).add(s)
        # no need to put list back into map since pass by reference 
    return [map.values()]
    

