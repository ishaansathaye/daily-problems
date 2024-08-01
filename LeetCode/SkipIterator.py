class SkipIterator:

    nativeIt = None
    nextEl = None # next element of skip iterator (not native)
    hMap = {}

    def __init__(self, Iterator it):
        # set the first nextEl
        self.advance()
        self.nativeIt = it

    def advance(self):
        '''Advances the Native Iterator'''
        nextEl = None
        while nextEl is None and nativeIt.hasNext():
            el = nativeIt.next()
            if el in self.hMap:
                self.hMap[el] -= 1
                if self.hMap[el] == 0:
                    self.hMap.remove(el)
            else:
                nextEl = el
    
    def skip(self, num):
        if nextEl == num:
            self.advance()
        else:
            if num in self.hMap:
                self.hMap[num] += 1
            else:
                self.hMap[num] = 1

    def hasNext():
        return nextEl is not None
    
    def next():
        re = nextEl
        self.advance
        return re
