class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * n + [0]
        for i in range(n - 1, -1, -1):
            take = 0
            for j in range(3):
                if i + j < n:
                    take += stoneValue[i + j]
                    dp[i] = max(dp[i], take - dp[i + j + 1])    
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"