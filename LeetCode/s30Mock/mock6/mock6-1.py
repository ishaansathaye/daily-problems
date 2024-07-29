class Logger:

    def __init__(self):
        self.hMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        '''At Mock'''
        print(self.hMap)
        if message in self.hMap:
            if timestamp - self.hMap[message] >= 10:
                self.hMap[message] = timestamp
                return True
        else:
            self.hMap[message] = timestamp
            return True

    def _shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        '''After'''
        if message in self.hMap:
            if timestamp >= self.hMap[message]:
                self.hMap[message] = timestamp+10
                return True
            else:
                return False
        self.hMap[message] = timestamp+10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
