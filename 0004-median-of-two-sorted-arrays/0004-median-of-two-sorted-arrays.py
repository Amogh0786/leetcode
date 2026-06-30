class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mer = sorted(nums1 + nums2)
        mid = len(mer) // 2
        if len(mer) % 2 == 0:
            return float((mer[mid-1] + mer[mid]) / 2)
        else:
            return float(mer[mid])  