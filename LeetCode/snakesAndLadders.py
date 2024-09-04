from typing import List
import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        '''BFS'''
        # null check
        n = len(board[0])
        arr = [0]*(n*n)

        # start
        r = n-1
        c = 0
        direction = True  # going from left to right
        idx = 0  # idx on 1D arr

        # flatten the 2D arr
        while idx < len(arr):
            if board[r][c] == -1:
                arr[idx] = board[r][c]
            else:
                # if a snake or ladder put destination in arr
                # dest - 1 is the idx in the board
                arr[idx] = board[r][c] - 1
            idx += 1
            if direction:
                c += 1
                if c == n:
                    direction = False
                    r -= 1
                    c -= 1  # stay within limits
            else:
                c -= 1
                if c < 0:
                    direction = True
                    r -= 1
                    c += 1

        # bfs
        moves = 0
        q = deque()  # indices of 1D array
        q.append(0)
        arr[0] = -2  # mark as visited
        while len(q) != 0:
            size = len(q)
            # process level
            for i in range(size):
                currIdx = q.popleft()
                if currIdx >= n*n - 1:
                    return moves
                # roll the dice
                for k in range(1, 7):
                    newIdx = currIdx+k
                    # already reached destination
                    if newIdx == n*n:
                        break
                    # visited or not
                    if arr[newIdx] != -2:
                        if arr[newIdx] == -1:
                            q.append(newIdx)
                        else:
                            # if snake or ladder
                            # put that number at that index
                            q.append(arr[newIdx])
                        # mark as visited
                        arr[newIdx] = -2
            moves += 1

        return -1
