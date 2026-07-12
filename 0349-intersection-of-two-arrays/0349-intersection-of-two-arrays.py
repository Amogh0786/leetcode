class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h={}
        for i in nums1:
            if i not in h:
                h[i]=1
        for i in nums2:
            if i in h and h[i]==1:
                h[i]=2
        ans=[]
        for i in h:
            if h[i]==2:
                ans.append(i)
        return ans