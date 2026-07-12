class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if length == len(set(nums)):
            return False
        for i in range (len(nums)):
            if nums[i] in nums[i+1:i+k+1]:
                return True
        return False