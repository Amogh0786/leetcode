class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, max, min = 0, prices[0], prices[0]
        for p in prices:
            if p < min:
                if max - min > ans:
                    ans = max - min
                min = max = p
            elif p > max:
                max = p
        return ans if max - min < ans else max - min