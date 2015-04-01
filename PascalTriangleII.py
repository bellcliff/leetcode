class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex is 0:
            return [1]
        if rowIndex is 1:
            return [1, 1]
        row = self.getRow(rowIndex-1)
        for i in range(rowIndex / 2):
            idx0 = rowIndex / 2 - i
            idx1 = (rowIndex + 1) / 2 + i
            row[idx0] = row[idx1] = row[idx0 - 1] + row[idx0]
        row.append(1)
        return row

for i in range (10):
    print Solution().getRow(i)
