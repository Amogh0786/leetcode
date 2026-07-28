class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        for char in word:
            if char != ch:
                index += 1
            else:
                break
        if index != len(word) :
            rev = word[:index+1]
            return rev[::-1] + word[index+1:]
        else:
            return word