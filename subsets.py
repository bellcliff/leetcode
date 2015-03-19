class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        subs = [[]]
        for x in S:
            subs = self.subhelp(x, subs[:])
        return subs

    def subhelp(self, x, subs):
        subs1 = []
        for s in subs:
            subs1.append(s)
            subs1.append(self.insertSub(x, s[:]))
        return subs1

    def insertSub(self, x, s):
        inserted = False
        for i in range(len(s)):
            if x < s[i]:
                s.insert(i, x)
                inserted = True
                break
        if not inserted:
            s.append(x)
        return s[:]

print Solution().subsets([0,1,2,3,4,5,6,7,8,9,10, 0])
