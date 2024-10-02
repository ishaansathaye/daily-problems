# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def _findCelebrity(self, n: int) -> int:
        '''inDegrees Topological Sort'''
        '''Time Limit'''
        inDegrees = [0]*n
        for i in range(n):
            for j in range(i+1, n):
                if knows(i, j):
                    inDegrees[j] += 1
                    inDegrees[i] -= 1
                if knows(j, i):
                    inDegrees[i] += 1
                    inDegrees[j] -= 1

        for i in range(n):
            if inDegrees[i] == n-1:
                return i
        return -1

    def findCelebrity(self, n: int) -> int:
        '''2-Pass'''
        celeb = 0
        for i in range(n):
            if knows(celeb, i):
                celeb = i

        # potential celeb
        for i in range(n):
            if i == celeb:
                continue
            if not knows(i, celeb):
                return -1
            # checking those before celeb
            # reducing the number of API calls
            # only do when i < celeb
            if i < celeb and knows(celeb, i):
                return -1
        return celeb
