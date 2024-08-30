from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        # def sortHeight(a, b):
        #     if a[0] == b[0]:
        #         return a[1] - b[1]
        #     return b[0] - a[0]

        # people = sorted(people, key=cmp_to_key(sortHeight))
        # or
        people.sort(key=lambda x: (-x[0], x[1]))  # O(nlogn)
        li = []
        for person in people:
            # put it at index at how many people in front
            # O(n^2)
            li.insert(person[1], person)
        return li
