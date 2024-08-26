# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    '''Original Solution'''
    '''Non-lazy loading'''

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.arr = []
        while iterator.hasNext():
            self.arr.append(iterator.next())
        self.n = len(self.arr)
        self.i = 0

    def peek(self):
        """
        Returns the next element in the iteration without
        advancing the iterator.
        :rtype: int
        """
        return self.arr[self.i]

    def next(self):
        """
        :rtype: int
        """
        el = self.arr[self.i]
        self.i += 1
        return el

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i < self.n:
            return True
        return False


class _PeekingIterator:
    '''Lazy Loading Solution'''

    current = None
    iterator = None

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        if self.iterator.hasNext():
            self.current = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without
        advancing the iterator.
        :rtype: int
        """
        return self.current if self.current else None

    def next(self):
        """
        :rtype: int
        """
        el = self.current
        if self.iterator.hasNext():
            self.current = self.iterator.next()
        else:
            self.current = None
        return el

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.current is not None else False

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
