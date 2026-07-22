import math
class Solution:
    def maxLength(self, nums: list[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            p = l = 1
            g = 0
            for j in range(i, n):
                p *= nums[j]
                if p > 25200: 
                    break
                l = math.lcm(l, nums[j])
                g = math.gcd(g, nums[j])
                if p == l * g:
                    ans = max(ans, j - i + 1)
        return ans