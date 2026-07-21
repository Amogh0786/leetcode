class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0: 
            return False
        if valueDiff == 0:
            seen: dict[int, int] = {}
            for i, n in enumerate(nums):
                if n in seen and i - seen[n] <= indexDiff:
                    return True
                seen[n] = i
            return False
        w = valueDiff + 1
        buckets: dict[int, int] = {}
        def bucket_id(x: int) -> int:
            return x // w if x >= 0 else (x + 1) // (w - 1)
        for i, num in enumerate(nums):
            bid = bucket_id(num)
            if bid in buckets:
                return True
            if bid - 1 in buckets and abs(buckets[bid - 1] - num) <= valueDiff:
                return True
            if bid + 1 in buckets and abs(buckets[bid + 1] - num) <= valueDiff:
                return True
            buckets[bid] = num
            if i >= indexDiff:
                del buckets[bucket_id(nums[i - indexDiff])]
        return False