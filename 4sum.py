class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        sub = dict()
        res = []
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                k = num[i] + num[j]
                if k not in sub:
                    sub[k] = []
                sub[k].append([i,j])
        print sub
        for k in sub:
            mk = target - k
            if mk in sub:
                for i, j in sub.get(k):
                    for k, l in sub.get(mk):
                        item = sorted([num[i], num[i], num[k], num[l]])
                        if i != k and i !=l and j != k and j != l and item not in res:
                            res.append(item)

        return res

print Solution().fourSum([0,0,0,0], 0)
