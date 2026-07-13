class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c, m = 0, nums[0]
        for num in nums:
            if c < 0: c = 0
            c += num
            if c > m: m = c
        return m