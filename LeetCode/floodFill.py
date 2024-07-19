from typing import List


class Solution:
    def _floodFill(self, image: List[List[int]], sr: int,
                   sc: int, color: int) -> List[List[int]]:
        '''BFS Approach'''
        if image is None:
            return image
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m = len(image)
        n = len(image[0])
        startColor = image[sr][sc]
        if image[sr][sc] == color:
            return image
        q = []  # of type integers
        q.append(sr)
        q.append(sc)
        image[sr][sc] = color
        while len(q) != 0:
            # size not required in this problem
            cr = q.pop(0)
            cc = q.pop(0)
            for d in dirs:
                nr = d[0] + cr
                nc = d[1] + cc
                # bounds check
                if (nr >= 0 and nc >= 0 and nr < m and nc < n
                        and image[nr][nc] == startColor):
                    q.append(nr)
                    q.append(nc)
                    # change color here after adding into q
                    image[nr][nc] = color
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc:
                  int, color: int) -> List[List[int]]:
        '''DFS Approach'''
        if image is None:
            return image
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        startColor = image[sr][sc]
        if image[sr][sc] == color:
            return image
        self.dfs(image, sr, sc, startColor, color, dirs)
        return image

    def dfs(self, image, r, c, startColor, color, dirs):
        # base
        if (r < 0 or c < 0 or r == len(image)
                or c == len(image[0]) or image[r][c] != startColor):
            return

        # logic
        image[r][c] = color
        for d in dirs:
            nr = d[0] + r
            nc = d[1] + c
            self.dfs(image, nr, nc, startColor, color, dirs)
