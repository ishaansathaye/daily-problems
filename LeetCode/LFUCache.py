from collections import defaultdict


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
        self.next = None
        self.prev = None


class DLL:

    def __init__(self):
        self.head = Node(-1, -1)  # dummy
        self.tail = Node(-1, -1)  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addToHead(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        self.size += 1

    def removeNode(self, node: Node) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def removeTail(self) -> Node:
        # func for remove the key from main map
        tailPrev = self.tail.prev
        self.removeNode(tailPrev)
        return tailPrev


class LFUCache:

    def __init__(self, capacity: int):
        self.nodeMap = defaultdict(Node)
        self.freqMap = defaultdict(DLL)
        self.capacity = capacity
        self.min = 0

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.updateNode(node)
        return node.val

    def updateNode(self, node):
        '''moves node from old freq list to new freq list
        in freqMap'''
        oldCount = node.count
        oldList = self.freqMap[oldCount]
        oldList.removeNode(node)
        # if self.min list is empty and count to remove is min
        if oldCount == self.min and oldList.size == 0:
            self.min += 1
        node.count += 1
        # ore create new one (done by defaultdict)
        newList = self.freqMap[node.count]
        newList.addToHead(node)
        self.freqMap[node.count] = newList

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            # existing node
            node = self.nodeMap[key]
            node.val = value
            self.updateNode(node)
        else:
            # fresh
            # if capacity of cache is full
            if self.capacity == len(self.nodeMap):
                # remove lru node (the tail basically)
                minList = self.freqMap[self.min]
                toRemove = minList.removeTail()
                del self.nodeMap[toRemove.key]
            newNode = Node(key, value)
            self.min = 1
            # or create new one (done by defaultdict)
            newList = self.freqMap[self.min]
            newList.addToHead(newNode)
            self.freqMap[1] = newList
            self.nodeMap[key] = newNode


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
