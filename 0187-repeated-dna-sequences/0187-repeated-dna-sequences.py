class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            pat = s[i:i+10]
            if pat in seen:
                repeated.add(pat)
            else:
                seen.add(pat)
        return list(repeated)