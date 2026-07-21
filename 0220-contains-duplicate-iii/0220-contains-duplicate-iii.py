class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        d, w = {}, valueDiff + 1
        for i, x in enumerate(nums):
            b = x // w
            if any(c in d and abs(x - d[c]) <= valueDiff for c in (b - 1, b, b + 1)):
                return True
            d[b] = x
            if i >= indexDiff:
                del d[nums[i - indexDiff] // w]  
        return False