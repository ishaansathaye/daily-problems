class Solution:
    def __isRobotBounded(self, instructions: str) -> bool:
        '''Original Solution'''
        pos = [0, 0]
        d = 0
        n = len(instructions)
        for i in range(n):
            s = instructions[i]
            if s == 'G':
                if d == 0:
                    pos[1] += 1
                elif abs(d) == 180:
                    pos[1] -= 1
                elif d == -90 or d == 270:
                    pos[0] -= 1
                elif d == 90 or d == -270:
                    pos[0] += 1
            elif s == 'L':
                d -= 90
            elif s == 'R':
                d += 90
            if abs(d) == 360:
                d = 0
        # added d != 0 logic from s30
        if pos == [0, 0] or d != 0:
            return True
        return False

    def _isRobotBounded(self, instructions: str) -> bool:
        '''4 Runs of Instructions Algo'''
        n = len(instructions)
        x = 0
        y = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx = 0  # initial direction of robot (north)
        for i in range(4):
            for j in range(n):
                c = instructions[j]
                if c == 'G':
                    x += dirs[idx][0]
                    y += dirs[idx][1]
                elif c == 'L':
                    idx = (idx+3) % 4
                else:
                    idx = (idx+1) % 4
            if x == 0 and y == 0:
                return True
        return False

    def isRobotBounded(self, instructions: str) -> bool:
        '''Not facing North Algo'''
        n = len(instructions)
        x = 0
        y = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx = 0  # initial direction of robot (north)
        for j in range(n):
            c = instructions[j]
            if c == 'G':
                x += dirs[idx][0]
                y += dirs[idx][1]
            elif c == 'L':
                idx = (idx+3) % 4
            else:
                idx = (idx+1) % 4
        # back at origin or not facing north
        # not facing north means it will
        # eventually return to origin
        if (x == 0 and y == 0) or (idx != 0):
            return True
        return False
