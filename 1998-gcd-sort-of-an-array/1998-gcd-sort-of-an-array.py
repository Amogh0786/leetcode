class Solution:
    def gcdSort(self, nums: list[int]) -> bool:
        m = max(nums)
        uf, spf = list(range(m + 1)), list(range(m + 1))
        def find(i):
            if uf[i] != i:
                uf[i] = find(uf[i])
            return uf[i]
        for i in range(2, int(m**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, m + 1, i):
                    if spf[j] == j: spf[j] = i    
        for x in nums:
            temp = x
            while temp > 1:
                uf[find(x)] = find(spf[temp])
                temp //= spf[temp]
        return all(find(a) == find(b) for a, b in zip(nums, sorted(nums)))