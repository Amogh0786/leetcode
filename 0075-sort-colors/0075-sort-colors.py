class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            swap = False
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
            if not swap:
                break