class Solution(object):
    def isOneBitCharacter(self, bits):
        i=0
        while i<len(bits)-1:
            if bits[i]==0:
                i+=1
                if i>=len(bits):break
            else:
                i+=2
                if i>=len(bits):break
        if i==len(bits)-1:return True
        else:return False