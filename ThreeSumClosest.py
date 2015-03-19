class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        _min = None
        num.sort()
        result = 0
        for i in range(len(num)-3):
            j = i + 1
            k = len(num) - 1
            while j < k:
                _sum = num[i] + num[j] + num[k]
                _diff = _sum - target
                if _diff is 0:
                    return target
                if _min is None or abs(_diff) < _min:
                    _min = abs(_diff)
                    result = _sum
                if _sum <= target:
                    j += 1
                else:
                    k -= 1
        return result

print Solution().threeSumClosest([1,1,1,0], 100)
