class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if self.isBiggest(num):
            reversed(num)
            return num
        else:
            for i in range(len(num)-1, 0, -1):
                if num[i] > num[i-1]:
                    num[i], num[i-1] = num[i-1], num[i]
                    return num

    def isBiggest(self, num):
        for i in range(len(num) - 1):
            if num[i] < num[i-1]:
                return False
        return True

    def all(self, num):
        res = [num]
        if len(num) <= 1:
            return res
        for i in range(len(num)):
            nc = num[:]
            del nc[i]
            for r in self.all(nc):
                for j in range(len(r)):
                    r1 = r[:]
                    r1.insert(j, num[i])
                    res.append(r1)
        return res

tests = [[1,2,3], [2,3,1], [3,1,2], [1,3,2]]
for t in tests:
    t1 = Solution().nextPermutation(t[:])
    print '%s %s %s' % (str(t), str(t1), t1 > t)
