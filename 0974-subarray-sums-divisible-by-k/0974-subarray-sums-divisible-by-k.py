class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix, count = 0, 0
        mp = {0:1}
        for i in nums:
            prefix += i
            rem = prefix % k
            count += mp.get(rem, 0)
            mp[rem] = mp.get(rem, 0) + 1
        return count