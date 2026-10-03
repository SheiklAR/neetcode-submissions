class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        ans = 0

        def mark_water(r, c):
            if (
                not 0 <= r < ROWS or 
                not 0 <= c < COLS or
                grid[r][c] == '0'
            ):
                return
            grid[r][c] = '0'
            
            for i,j in dirs:
                nr, nc = r+i, c+j
                mark_water(nr, nc)
        

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    ans += 1
                    mark_water(row, col)
        
        return ans