class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        f1=[0]*26
        f2=[0]*26
        for i in range(len(s)):
            f1[ord(s[i])-97]+=1
            f2[ord(t[i])-97]+=1
        for i in range(26):
            if f1[i]!=f2[i]:
                return False
        return True