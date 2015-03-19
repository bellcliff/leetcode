class Solution:
    # @return an integer
    def lengthOfLongestSubstringOld(self, s):
        if len(s) is 0:
            return 0
        d = dict()
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                subs = s[i:j]
                if len(subs) == len(set(subs)) and subs not in d:
                    d[subs] = len(subs)
        maxl = 0
        maxs = ''
        for k, v in d.items():
            if maxl < v:
                maxs = k
                maxl = v
        return maxs

    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        d = {s[0]: 0}
        curl = 1
        maxl = 1
        for i in range(1, len(s)):
            c = s[i]
            if c not in d or i - curl > d[c]:
                curl += 1
            else:
                if curl > maxl:
                    maxl = curl
                curl = i - d[c]
            d[c] = i
        return max(curl, maxl)


print Solution().lengthOfLongestSubstring('mitpxltadcsyzdszbpwnfojodbqnhduvnplmagpdljcknwmqokdtaohfpzsyemwsbjecpthcdjpsibkwnqpneyswxl')
