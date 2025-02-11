class Solution:
    def _convert(self, s: str, numRows: int) -> str:
        '''Original: TC=O(#rows*n)'''
        if numRows == 1:
            return s
        numCols = len(s)//2
        mat = [["" for _ in range(numCols+1)] for _ in range(numRows)]
        r = 0
        c = 0
        dr = 1
        dc = 0
        for char in s:
            mat[r][c] = char
            r += dr
            c += dc
            if r == numRows:
                dr = -1
                r -= 2
                c += 1
                dc += 1
            elif r < 0:
                r += 2
                c -= 1
                dr = 1
                dc = 0

        # res = []
        res = ""
        for r in mat:
            res += "".join(r)

        print(mat)
        return "".join(res)

    def convert(self, s: str, numRows: int) -> str:
        '''String Traversal: O(n)'''
        if numRows == 1:
            return s

        res = []
        n = len(s)
        # calc # of chars in each section
        # section being col+diagonal
        chars_section = 2*(numRows-1)

        # iterate thorugh each row
        for cr in range(numRows):
            idx = cr

            # start hopping to next section
            while idx < n:
                res.append(s[idx])

                # check if current row is first or last
                # special case where those 2 are identical jumps
                if cr != 0 and cr != numRows - 1:
                    # how much to jump to get to next char
                    new_idx = idx + (chars_section - 2*cr)
                    # as long as less than length of s add to res
                    if new_idx < n:
                        res.append(s[new_idx])

                # go to next section
                idx += chars_section

        return "".join(res)


'''
'P', ' ', ' ', 'I', ' ', ' ', 'N', ' '],
'A', ' ', 'L', 'S', ' ', 'I', 'G', ' '],
'Y', 'A', ' ', 'H', 'R', ' ', ' ', ' '],
'P', ' ', ' ', 'I', ' ', ' ', ' ', ' ']]
'''

if __name__ == "__main__":
    s = Solution()
    print(s._convert("PAYPALISHIRING", 4))
