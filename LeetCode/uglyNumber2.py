import heapq


class Solution:
    def _nthUglyNumber(self, n: int) -> int:
        '''O(nlongm)'''
        hSet = set()
        pq = []
        primes = [2, 3, 5]
        count = 0
        currUgly = 1
        heapq.heappush(pq, currUgly)
        while count < n:
            # increase count everytime popped
            currUgly = heapq.heappop(pq)
            count += 1
            # get factors of each prime for curr ugly num
            for prime in primes:
                newUgly = currUgly*prime
                if newUgly not in hSet:
                    hSet.add(newUgly)
                    heapq.heappush(pq, newUgly)
        return currUgly

    def nthUglyNumber(self, n: int) -> int:
        '''DP with Pointers'''
        # Pointers for each Prime Factor
        p2 = 0
        p3 = 0
        p5 = 0
        # arr to keep ugly numbers
        arr = [0 for _ in range(n)]
        arr[0] = 1
        # Pointers for all ugly numbers being calculated
        n2 = 2
        n3 = 3
        n5 = 5
        for i in range(1, n):
            minUgly = min(n2, n3, n5)
            arr[i] = minUgly
            # multiple ifs take care of duplicate mins
            if minUgly == n2:
                p2 += 1
                # multiply by 2 to get new ugly number
                n2 = arr[p2]*2
            if minUgly == n3:
                p3 += 1
                n3 = arr[p3]*3
            if minUgly == n5:
                p5 += 1
                n5 = arr[p5]*5
        return arr[-1]
