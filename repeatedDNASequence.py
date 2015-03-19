class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        res = dict()
        for i in range(len(s) - 9):
            subs = s[i:i+10]
            if subs not in res:
                res[subs] = 0
            else:
                res[subs] +=1
        print res
        return [k for k,v in res.items() if v >= 1]

print Solution().findRepeatedDnaSequences('AAAAAAAAAAA')
