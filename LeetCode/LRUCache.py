class Node:

    def __init__(self, key, value):
        '''Doubly Linked List'''
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hMap = {}

    def removeNode(self, node: Node):
        node.next.prev = node.prev
        node.prev.next = node.next
        # prevent memory leakage:
        node.next = None
        node.prev = None

    def addToHead(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key not in self.hMap:
            return -1
        node = self.hMap[key]
        # remove from current and add to start
        # since most recently used
        self.removeNode(node)
        self.addToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hMap:  # not fresh node
            # updating value also implemented:
            node = self.hMap[key]
            node.val = value
            self.removeNode(node)
            self.addToHead(node)
        else:  # if fresh node
            # if ll is full
            if len(self.hMap) == self.capacity:
                # remove lru
                tailPrev = self.tail.prev
                # remove from both:
                self.removeNode(tailPrev)
                del self.hMap[tailPrev.key]
            # add new node to both
            newNode = Node(key, value)
            self.addToHead(newNode)
            self.hMap[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
