class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        cs = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        _is = []
        for c in digits:
            _is.append(int(c))
        rs = []
        for _i in _is:
            rs = self.x(rs, list(cs[_i]))
        return rs

    def x(self, s1, s2):
        if s1 is None or len(s1) is 0:
            return s2
        if s2 is None or len(s2) is 0:
            return s1
        rs = []
        for a in s1:
            for b in s2:
                rs.append(a+b)
        return rs
