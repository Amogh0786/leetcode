from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        window_counts = {}
        formed = 0
        l = 0
        ans = float("inf"), None, None
        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            while l <= r and formed == required:
                char_l = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[char_l] -= 1
                if char_l in dict_t and window_counts[char_l] < dict_t[char_l]:
                    formed -= 1
                l += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]