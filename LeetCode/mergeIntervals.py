from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''O(nlogn)'''
        if len(intervals) == 1:
            return intervals
        # sorted so all starting are increasing
        intervals.sort(key=lambda x: x[0])
        res = []
        for elem in intervals:
            # check if empty or last interval max is < start of i interval
            if res == [] or res[-1][1] < elem[0]:
                res.append(elem)
            else:
                # correct max of last interval to be between max of
                # current and new interval's max
                res[-1][1] = max(res[-1][1], elem[1])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [4, 5]]))
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge([[1, 3], [8, 10], [2, 6], [15, 18]]))

'''
[[1,3], [2,6], [4,5]] -> [1, 6]

[[1,4], [2,6], [8, 10], [15, 18]]

[[1,4], [2,3], [8,10], [15,18]] i cannot exceed 3

'''
