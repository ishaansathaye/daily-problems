class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c)-ord('a')] is None:
                curr.children[ord(c)-ord('a')] = TrieNode()
            curr = curr.children[ord(c)-ord('a')]
        curr.isEnd = True

    # original dfs
    # def search(self, word: str) -> bool:
    #     curr = self.root
    #     return self.dfs(word, curr)
    #
    # def dfs(self, word, curr):
    #     for i in range(len(word)):
    #         c = word[i]
    #         if c == '.':
    #             # check at every level if char is .
    #             for node in curr.children:
    #                 if node is not None and self.dfs(word[i+1:], node):
    #                     return True
    #             return False
    #         elif curr.children[ord(c)-ord('a')] is None:
    #             return False
    #         curr = curr.children[ord(c)-ord('a')]
    #     return curr.isEnd

    # cleaner dfs
    def search(self, word: str) -> bool:
        curr = self.root
        return self.dfs(word, curr, 0)

    def dfs(self, word, curr, idx):
        if idx == len(word):
            return curr.isEnd

        c = word[idx]
        if c == '.':
            # check at every level if char is .
            for node in curr.children:
                if node and self.dfs(word, node, idx+1):
                    return True
            return False
        else:
            child = curr.children[ord(c)-ord('a')]
            if not child:
                return False
            return self.dfs(word, child, idx+1)

# Faster Runtime using Dictionary


class fTrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class fWordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    # original dfs
    def search(self, word: str) -> bool:
        curr = self.root
        return self.dfs(word, curr)

    def dfs(self, word, curr):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                # check at every level if char is .
                for node in curr.children:
                    if (node is not None and
                            self.dfs(word[i+1:], curr.children[node])):
                        return True
                return False
            elif c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
