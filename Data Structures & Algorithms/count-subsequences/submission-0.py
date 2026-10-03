class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for k in range(M+1):
            dp[k][-1] = 1
        
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][0]
        # d = {}

        # def dfs(i, j):
        #     if (i,j) in d:
        #         return d[(i,j)]

        #     if j == len(t):
        #         return 1
        #     if i >= len(s) or j >= len(t):
        #         return 0

        #     res = 0

        #     if s[i] == t[j]:
        #         res += dfs(i+1, j+1)

        #     res += dfs(i+1, j)
            
        #     d[(i,j)] = res
        #     return res
        

        # return dfs(0, 0)