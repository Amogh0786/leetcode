class Solution(object):
    def minBitFlips(self, start, goal):
        x = start ^ goal
        return bin(x).count('1')