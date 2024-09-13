from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        blocks = []
        n = len(s)
        i = 0
        while i < n:
            currBlock = []
            if s[i] == '{':
                i += 1
                while s[i] != '}':
                    # keep adding char in curr block
                    if s[i] != ',':
                        currBlock.append(s[i])
                    i += 1
            else:
                currBlock.append(s[i])
            # sort the curr block so that answer is sorted
            # when paths are made
            blocks.append(sorted(currBlock))
            i += 1

        # backtracking:
        res = []
        # self.backtrack(blocks, 0, [], res)
        self.backtrack(blocks, 0, "", res)
        return res

    def backtrack(self, blocks, idx, path, res):
        # base
        if idx >= len(blocks):
            # res.append("".join(path))
            res.append(path)
            return

        # logic when we are at ith block
        currBlock = blocks[idx]
        for i in range(len(currBlock)):
            # action
            # path.append(currBlock[i])
            path += currBlock[i]
            # recurse
            # used a block so go to next block (idx+1)
            self.backtrack(blocks, idx+1, path, res)
            # backtrack
            # path.pop(len(path)-1)
            path = path[0:len(path)-len(currBlock[i])]
