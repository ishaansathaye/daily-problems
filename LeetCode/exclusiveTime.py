from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for _ in range(n)]
        st = []  # of integers (can also have timestamp inside)
        # keep 2 variables for curr and prev timestamps
        curr, prev = 0, 0
        for log in logs:
            strArr = log.split(":")
            currTask = int(strArr[0])
            curr = int(strArr[2])
            # start log
            if strArr[1] == "start":
                if len(st) != 0:
                    # every start update with curr-prev times
                    res[st[-1]] += curr - prev
                # put in start
                st.append(currTask)
                # update prev time
                prev = curr
            else:
                # end log
                # +1 because of right border
                res[st.pop()] += curr + 1 - prev
                prev = curr + 1
        return res
