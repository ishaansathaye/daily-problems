from typing import List


class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.isStart = False


class StreamChecker:

    def insert(self, root, word):
        curr = root
        for i in range(len(word)-1, -1, -1):
            c = word[i]
            if curr.children[ord(c) - ord('a')] is None:
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.isStart = True

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.sb = []
        self.maxVal = -2**31
        for word in words:
            self.insert(self.root, word)
            self.maxVal = max(self.maxVal, len(word))

    def query(self, letter: str) -> bool:
        self.sb.append(letter)
        curr = self.root
        # Optimization: keeping sb at max length of word in words
        if len(self.sb) > self.maxVal:
            self.sb.pop(0)
        for i in range(len(self.sb)-1, -1, -1):
            ch = self.sb[i]
            if curr.children[ord(ch) - ord('a')] is None:
                return False
            curr = curr.children[ord(ch) - ord('a')]
            if curr.isStart:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
