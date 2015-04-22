class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        a,b,c = {}, {}, {}   # means line, height and cube
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                # v shouldn't in a, b, c
                if v == '.':  # ignore empty cell
                    continue

                if i not in a:  # if a is empty
                    a[i] = [v]
                elif v in a[i]:
                    return False
                else:
                    a[i].append(v)

                if j not in b:
                    b[j] = [v]
                elif v in b[j]:
                    return False
                else:
                    b[j].append(v)

                k = '%d_%d' % (i/3, j/3)
                if k not in c:
                    c[k] = [v]
                elif v in c[k]:
                    return False
                else:
                    c[k].append(v)
        return True
