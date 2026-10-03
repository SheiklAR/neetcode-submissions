class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]

        for i in range(N1-1, -1, -1):
            for j in range(N2-1, -1, -1): 
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]