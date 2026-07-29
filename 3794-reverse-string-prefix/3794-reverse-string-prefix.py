class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        rev = s[:k]
        return rev[::-1] + s[k:]