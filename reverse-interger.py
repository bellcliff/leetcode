class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        isNegative = x < 0
        x = abs(x)
        temp = 0
        while x > 0:
            temp = temp * 10 + x % 10
            x = x / 10
        if isNegative:
            temp *= -1
        return temp

print Solution().reverse(-10)
