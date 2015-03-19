class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        result = []
        if k == 1:
            return [[i] for i in range(1, n+1)]
        else:
            A = self.combine(n, k-1)
            for a in A:
                for i in range(max(a)+1, n+1):
                    result.append(a + [i])

        return result

print Solution().combine(2,1)
