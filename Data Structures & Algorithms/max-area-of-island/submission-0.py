class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS =  len(grid), len(grid[0])
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]

        ans = 0

        def bfs(r, c):
            dq = deque([(r, c)]) # If stack used it will be dfs
            area = 1
            while dq:
                # print('here')
                r, c = dq.popleft()
                
                for row, col in dirs:
                    nr, nc = r + row, c + col
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        area += 1
                        grid[nr][nc] = 0
                        dq.append((nr, nc))
            
            return area


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = max(ans, bfs(i, j))
        
        return ans


        # ROWS, COLS =  len(grid), len(grid[0])
        # ans = 0
        # dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]

        # def dfs(r, c):
        #     if not 0 <= r < ROWS or not 0 <= c < COLS or grid[r][c] == 0:
        #         return 0
            
        #     res = 1
        #     grid[r][c] = 0

        #     for row, col in dirs:
        #         nr, nc = r + row, c + col
        #         res += dfs(nr, nc)
            
        #     return res
        
        
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         ans = max(ans, dfs(i, j))
        

        # return ans