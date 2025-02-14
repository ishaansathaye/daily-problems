class MinStack:

    def __init__(self):
        self.st = []
        self.len = 0

    def push(self, val: int) -> None:
        # just keeping track of min until that element
        # check for top of stack for current minimum
        if not self.st or self.st[-1][1]:
            self.st.append((val, val))
        else:
            self.st.append((val, self.st[-1][1]))
        self.len += 1

    def pop(self) -> None:
        self.st = self.st[:self.len-1]
        self.len -= 1

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


'''

(1,1) (2,1) (3,1) (4,1) (5,1)
-2 0 -3 -> (-2, -2) (0, -2) (-3 -3)
0 1 0 -> (0, 0) (1, 0) (0, 0)

-10 14 getMin=-10 getMin=-10 -20 -20*4 pop=20gone (10, -10) (-7, -10)
'''

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    obj = MinStack()
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]]
    print(obj.push(-2))
    print(obj.push(0))
    print(obj.push(-3))
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
    print()
    obj = MinStack()
    print(obj.push(0))
    print(obj.push(1))
    print(obj.push(0))
    print(obj.getMin())
    print(obj.pop())
    print(obj.getMin())
