from collections import deque


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.hSet = set()
        self.q = deque()
        for i in range(0, maxNumbers):
            self.hSet.add(i)
            self.q.append(i)

    def get(self) -> int:
        if len(self.q) == 0:
            return -1
        re = self.q.pop()
        self.hSet.remove(re)
        return re

    def check(self, number: int) -> bool:
        return number in self.hSet

    def release(self, number: int) -> None:
        if number not in self.hSet:
            self.hSet.add(number)
            self.q.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
