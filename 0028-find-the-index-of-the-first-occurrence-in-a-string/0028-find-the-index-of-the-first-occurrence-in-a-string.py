class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        p = len(needle)
        for i in range(n):
            if needle == haystack[i:p+i]:
                return i
        return -1