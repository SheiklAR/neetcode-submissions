class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def crossedBoundary(r, c):
            if r < 0 or c < 0 or r == ROW or c == COL:
                return True
            return False
            
        
        def dfs(r, c, cnt):
            if crossedBoundary(r, c) or grid[r][c] == -1:
                return inf
            
            if grid[r][c] == 0:
                return cnt
            
            visited.add((r, c))
            ans = inf

            for (i, j) in dirs:
                next_r, next_c = i + r, j + c
                if (next_r, next_c) not in visited:

                    ans = min(ans, dfs(next_r, next_c, cnt + 1))

            visited.remove((r, c))
            return ans


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == inf:
                    grid[row][col] = dfs(row, col, 0)

