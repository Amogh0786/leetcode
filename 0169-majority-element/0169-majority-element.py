class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        newset = list(set(nums))
        for i in range(len(newset)):
            if nums.count(newset[i]) > len(nums) / 2:
                return newset[i]