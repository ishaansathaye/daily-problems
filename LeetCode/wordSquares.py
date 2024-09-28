from typing import List
# from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.li = []
        # self.children = defaultdict()
        self.children = [None for _ in range(26)]


class Solution:
    def insert(self, root, word):
        curr = root
        for i in range(0, len(word)):
            c = word[i]
            if curr.children[ord(c)-ord('a')] is None:
                curr.children[ord(c)-ord('a')] = TrieNode()
            # if c not in curr.children:
            #     curr.children[c] = TrieNode()
            # move current TrieNode down the chain
            curr = curr.children[ord(c)-ord('a')]
            # add the word to the list at that letter
            curr.li.append(word)

    def search(self, root, prefix):
        curr = root
        for i in range(0, len(prefix)):
            c = prefix[i]
            if curr.children[ord(c)-ord('a')] is None:
                return []
            # if c not in curr.children:
            #     return []
            # move current TrieNode down the chain
            curr = curr.children[ord(c)-ord('a')]
        # getting all the words at that prefix (letter(s))
        return curr.li

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        root = TrieNode()
        for word in words:  # O(n*k)
            self.insert(root, word)
        path = []
        # try every word as the first word
        for word in words:
            # action
            path.append(word)
            # recurse
            self.backtrack(root, path, res)
            # backtrack
            path.pop(len(path)-1)
        return res

    # path is the current path
    def backtrack(self, root, path, res):
        # base
        if len(path) == len(path[0]):
            res.append(path.copy())
            return

        # logic
        # make the prefix
        prefix = ""
        k = len(path)
        for word in path:
            prefix += word[k]

        # get the path with all words that start with prefix
        startsWith = self.search(root, prefix)

        for word in startsWith:
            # action
            path.append(word)
            # recurse
            self.backtrack(root, path, res)
            # backtrack
            path.pop(len(path)-1)
