from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            flag = False
            j = 0  # pointer on pattern
            for i in range(len(query)):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                    # at the end means pattern fulfilled
                    # but if more chars after -> false in elif
                    if j == len(pattern):
                        flag = True
                elif query[i].isupper():
                    flag = False
                    break
            res.append(flag)
        return res
