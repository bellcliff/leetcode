class Solution:
    # @return an integer
    def threeSum(self, num):
        num.sort()
        rs = []
        for i in range(len(num)-2):
            a = num[i]
            start = i+1
            end = len(num) - 1
            while start < end:
                b = num[start]
                c = num[end]
                if a+b+c == 0:
                    if [a,b,c] not in rs:
                        rs.append([a,b,c])
                    start = start + 1
                    end = end - 1
                elif a+b+c > 0:
                    end = end -1
                else:
                    start = start + 1
        return rs

print Solution().threeSum([-1, 0, 1, 2, -1, -4])
