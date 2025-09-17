from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = 0
        for x in nums:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best
