class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        newset = list(set(nums))
        o = len(nums)/2
        for i in range(len(newset)):
            if nums.count(newset[i]) > o:
                return newset[i]