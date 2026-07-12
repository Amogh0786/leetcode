class Solution(object):
    def numOfStrings(self, patterns, word):
        count=0
        for pt in patterns:
            if pt in word:
                count+=1
            else:
                pass
        return count