class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        M, N = len(matrix), len(matrix[0])
        ans = 0
        d = {}

        def dfs(r,c):
            key = (r,c)
            if key in d:
                return d[key]

            # if key in visited:
            #     return 0
            
            # visited.add(key)
            res = 0

            for i,j in dirs:
                nr, nc = i + r, j + c
                if 0 <= nr < M and 0 <= nc < N and  matrix[nr][nc] > matrix[r][c]:
                    res = max(res, dfs(nr, nc))
            
            # visited.remove(key)
            d[key] = 1 + res
            return d[key]

        
        
        for i in range(M):
            for j in range(N):
                # x = dfs(i,j)
                # print(x)
                ans = max(ans, dfs(i,j))
        
        return ans