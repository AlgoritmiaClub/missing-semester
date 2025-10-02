class Solution:
    def maxSubArray(self, nums):
        best = nums[0]
        cur = 0
        for x in nums:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best
