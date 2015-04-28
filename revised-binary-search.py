class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}

    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] <= nums[r]:  # splited
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m
            else:
                if target <= nums[m] and target >= nums[l]:
                    r = m
                else:
                    l = m + 1
        return l if nums[l] == target else -1

print Solution().search([2, 1], 1)
