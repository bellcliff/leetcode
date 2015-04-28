class Solution:
    # @param grid, a list of lists of integers
    # @return an integer

    def minPathSum(self, grid):
        h, v = len(grid), len(grid[0])
        res = [[0 for x in range(v)] for x in range(h)]
        res[0][0] = grid[0][0]
        for i in range(1, h):
            res[i][0] = grid[i][0] + res[i - 1][0]
        for i in range(1, v):
            res[0][i] = grid[0][i] + res[0][i - 1]
        for x in range(1, h):
            for y in range(1, v):
                res[x][y] = grid[x][y] + min(res[x - 1][y], res[x][y - 1])
        return res[h - 1][v - 1]

print Solution().minPathSum([[1, 2], [1, 1]])
