class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        INF = 2147483647
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if grid[r][c] == 0: return 0

            if grid[r][c] == -1:
                return INF
            
            if grid[r][c] != INF:
                return grid[r][c]
            
            visited.add((r, c))
            res = INF
            for row, col in dirs:
                nr, nc = row + r, col + c
                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
                    continue
                if (nr, nc) in visited:
                    continue
                res = min(res, dfs(nr, nc))
                
            if res != INF:
                grid[r][c] = 1 + res
            visited.remove((r, c))
            return grid[r][c]
            
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == INF:
                    dfs(r, c)
        
