class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s = s.lower().replace(" ", "")
        clean_text = s.translate(str.maketrans("", "", string.punctuation))
        ls = list(clean_text)
        return ls == ls[::-1]