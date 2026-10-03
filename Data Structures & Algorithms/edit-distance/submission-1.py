class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)

        dp = [[0] * (N + 1) for _ in range(M + 1)]

        #base cases like dfs
        for i in range(M, -1, -1):
            dp[i][-1] = M-i

        #base cases like dfs
        for j in range(N, -1, -1):
            dp[-1][j] = N-j
        
        #base cases like dfs
        dp[M][N] = 0

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i+1][j+1], dp[i][j+1])
        
        return dp[0][0]

        # def dfs(i,j):
        #     key = (i,j)
        #     if key in d:
        #         return d[key]
        #     if j >= len(word2) and i >= len(word1):
        #         return 0
            
        #     if j >= len(word2):
        #         # print(j,i)
        #         return len(word1) - i
            
        #     if i >= len(word1):
        #         return len(word2) - j

        #     res = float('inf')
        #     #equal
        #     if word1[i] == word2[j]:
        #         res = dfs(i+1, j+1)
        #     else:
        #         #delete
        #         # res1 = 1 + dfs(i+1, j)
        #         # #replace
        #         # res2 = 1 + dfs(i+1, j+1)
        #         # #insert
        #         # res3 = 1 + dfs(i, j+1)

        #         res = 1 + min(dfs(i+1, j), dfs(i+1, j+1), dfs(i, j+1))

        #     d[key] = res

        #     return d[key]

        
        # return dfs(0,0)