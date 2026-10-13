class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = (2 ** 31) - 1

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1:
                return INF
            if grid[r][c] == 0:
                return 0
            
            # if grid[r][c] != -1 and grid[r][c] != INF:
                # return grid[r][c]
            
            visited.add((r, c))
            
            for row, col in dirs:
                nr, nc = r + row, c + col
                if (nr, nc) not in visited:
                    grid[r][c] = min(grid[r][c], 1 + dfs(nr, nc))
            

            return grid[r][c]

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF or grid[i][j] > 0:
                    visited = set()
                    dfs(i, j)
        
        