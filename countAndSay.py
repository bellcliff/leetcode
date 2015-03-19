class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return '1'
        res = ''
        cm = self.countAndSay(n-1)
        i = 0
        while i < len(cm):
            j = i
            count = 1
            while j + 1 < len(cm) and cm[j] == cm[j+1]:
                j += 1
                count += 1
            res += str(count)
            res += cm[j]
            print '%d %d %d %s' % (n, count, j, res)
            i = j + 1
        return res

print Solution().countAndSay(6)


