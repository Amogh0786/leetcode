class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if x == 0 else 1 for x in nums]

        prefix = 0
        ans = 0
        mp = {0: -1}

        for i in range(len(nums)):
            prefix += nums[i]

            if prefix in mp:
                ans = max(ans, i - mp[prefix])
            else:
                mp[prefix] = i

        return ans