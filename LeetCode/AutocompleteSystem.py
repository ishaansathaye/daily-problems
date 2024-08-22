from typing import List
import heapq
import defaultdict


class HeapElement:
    def __init__(self, hotness, lex):
        self.hotness = hotness
        self.lex = lex

    def __lt__(self, other):
        if self.hotness == other.hotness:
            return self.lex > other.lex
        return self.hotness < other.hotness


class AutocompleteSystemPQ:

    def __init__(self, sentences: List[str], times: List[int]):
        self.hMap = defaultdict(int)
        self.inputC = ""  # StringBuilder in Java
        for i in range(len(times)):
            currStr = sentences[i]
            cnt = times[i]
            self.hMap[currStr] += cnt

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.hMap[self.inputC] += 1
            self.inputC = ""
            return []

        self.inputC += c
        pq = []
        for word in self.hMap.keys():
            if word.startswith(self.inputC):
                heapq.heappush(pq, HeapElement(self.hMap[word], word))
                if len(pq) > 3:
                    heapq.heappop(pq)
        res = []
        while len(pq) != 0:
            res.insert(0, heapq.heappop(pq).lex)
        return res


class TrieNode:

    def __init__(self):
        # can also be a hMap for children list
        # key is the character and value is the TrieNodes
        # self.children = {}
        self.children = [None for i in range(256)]  # all asci values
        self.startsWith = []


class AutocompleteSystemT:
    '''Optimized with Trie'''

    def __init__(self, sentences: List[str], times: List[int]):
        self.hMap = defaultdict(int)
        self.inputC = ""  # StringBuilder in Java
        self.root = TrieNode()
        for i in range(len(times)):
            currStr = sentences[i]
            cnt = times[i]
            # insert in map and trie
            if currStr not in self.hMap:
                # no need to put into trie for duplicate searches
                self.insert(self.root, currStr)
            self.hMap[currStr] += cnt

    def input(self, c: str) -> List[str]:
        if c == "#":
            if self.inputC not in self.hMap:
                self.insert(self.root, self.inputC)
            self.hMap[self.inputC] += 1
            # reset the search
            self.inputC = ""
            return []

        self.inputC += c
        pq = []
        # gives whole list in O(l)
        # no need to go over hashmap anymore
        startsWith = self.search(self.root, self.inputC)
        for word in startsWith:
            heapq.heappush(pq, HeapElement(self.hMap[word], word))
            if len(pq) > 3:
                heapq.heappop(pq)
        res = []
        while len(pq) != 0:
            res.insert(0, heapq.heappop(pq).lex)
        return res

    def insert(self, root, word):
        curr = root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c)-ord(' ')] is None:
                curr.children[ord(c)-ord(' ')] = TrieNode()
            curr = curr.children[ord(c)-ord(' ')]
            curr.startsWith.append(word)

    def search(self, root, prefix) -> List[str]:
        curr = root
        for i in range(len(prefix)):
            c = prefix[i]
            if curr.children[ord(c)-ord(' ')] is None:
                return []
            curr = curr.children[ord(c)-ord(' ')]
        return curr.startsWith


class TrieNodehMap:

    def __init__(self):
        # can also be a hMap for children list
        # key is the character and value is the TrieNodes
        self.children = {}
        self.top3 = []


class AutocompleteSystem:
    '''Further Optimized with just top 3 at each TrieNode,
    instead of all words'''

    def __init__(self, sentences: List[str], times: List[int]):
        self.hMap = defaultdict(int)
        self.inputC = ""  # StringBuilder in Java
        self.root = TrieNodehMap()
        for i in range(len(times)):
            currStr = sentences[i]
            cnt = times[i]
            # insert in map and trie
            self.hMap[currStr] += cnt
            self.insert(self.root, currStr)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.hMap[self.inputC] += 1
            # have to insert to bring it up in pq
            # after hMap because updating its count bef
            self.insert(self.root, self.inputC)
            # reset the search
            self.inputC = ""
            return []

        self.inputC += c
        return self.search(self.root, self.inputC)

    def insert(self, root, word):
        curr = root
        for i in range(len(word)):
            c = word[i]
            # for hMap children
            if c not in curr.children.keys():
                curr.children[c] = TrieNodehMap()
            curr = curr.children[c]
            # maintaining top3 in "pq"
            li = curr.top3  # by reference so no need to put back in
            if word not in li:
                li.append(word)
            # sorted based on hotness and lex
            li.sort(key=lambda x: (-self.hMap[x], x))  # O(3log3)
            if len(li) > 3:
                li.pop(len(li)-1)

    def search(self, root, prefix) -> List[str]:
        curr = root
        for i in range(len(prefix)):
            c = prefix[i]
            # for hMap children
            if c not in curr.children:
                return []
            curr = curr.children[c]
        # return [item[1] for item in curr.top3]
        return curr.top3

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
