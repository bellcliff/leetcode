
class Solution:

    # @param nums, an integer[]
    # @return an integer

    def findPeakElement(self, nums):
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        while l < r - 1:
            m = (l + r) / 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            if nums[m] > nums[m + 1]:
                r = m - 1
            else:
                l = m + 1
        return l if nums[l] > nums[r] else r

print Solution().findPeakElement([1, 2])
