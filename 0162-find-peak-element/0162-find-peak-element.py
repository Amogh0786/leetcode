class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return 0
        for i in range(n):
            if i==0:
                if nums[i]>nums[i+1]:
                    return i
                else:
                    continue
            if i==n-1:
                if nums[i]>nums[i-1]:
                    return i
                else:
                    continue
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i