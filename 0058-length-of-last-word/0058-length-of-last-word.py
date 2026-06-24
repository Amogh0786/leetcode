class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len = 0
        s = " ".join(s.split())
        for char in s[::-1]:
            if char != " ":
                len += 1
            else:
                return len
        return len    