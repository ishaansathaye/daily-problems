from typing import List


class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c)-ord('a')] is None:
                curr.children[ord(c)-ord('a')] = TrieNode()
            curr = curr.children[ord(c)-ord('a')]
        curr.isEnd = True


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        '''N*l + M*l = max() = O(N+M)'''
        root = TrieNode()

        for word in dictionary:
            root.insert(word)  # N*l

        result = ""
        strArr = sentence.split(' ')  # O(M)

        for i in range(len(strArr)):  # M
            word = strArr[i]
            replacement = ""
            curr = root
            if i != 0:
                result += " "
            for j in range(len(word)):  # l
                c = word[j]
                # break if these conditions: end or found replacement
                if (curr.children[ord(c)-ord('a')] is None
                        or curr.isEnd is True):
                    break
                replacement += c
                curr = curr.children[ord(c) - ord('a')]
            if curr.isEnd:
                result += replacement
            else:
                result += word
        return result

    def _replaceWords(self, dictionary: List[str], sentence: str) -> str:
        '''Hashset Only'''
        hSet = set(dictionary)  # N*l
        strArr = sentence.split(" ")

        result = ""
        for i in range(len(strArr)):  # M*l
            if i != 0:
                result += " "
            word = strArr[i]
            flag = False
            for j in range(len(word)):
                subStr = word[0:j+1]
                if subStr in hSet:
                    result += subStr
                    # do not go any further
                    flag = True
                if flag:
                    break
            if not flag:
                result += word
        return result
