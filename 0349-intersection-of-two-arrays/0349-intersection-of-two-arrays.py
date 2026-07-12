class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out=[]
        for i in nums1:
            if i in nums2:
                out.append(i)
        return list(set(out))