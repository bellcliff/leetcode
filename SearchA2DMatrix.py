class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) is 0:
            return False
        m = len(matrix)
        n = len(matrix[0])  # m, n: 1, 2
        l, r = 0, m * n - 1  # l, r: 0, 1
        while l != r:
            mid = (l + r) / 2  # mid: 0
            x, y = mid / n, mid % n
            if matrix[x][y] < target:
                l = mid + 1  # l, r: 1,1
            else:
                r = mid
        return matrix[r / n][r % n] == target

print Solution().searchMatrix([[1]], 1), True
print Solution().searchMatrix([[1]], 2), False
print Solution().searchMatrix([[1, 2]], 2), True
print Solution().searchMatrix([[1, 1]], 2), False
