class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dq = deque([])
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0, -1)]
        INF =  2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dq.append((r, c))

        print(dq)
        while dq:
            
            r,c = dq.popleft()

            for i,j in dirs:
                nr, nc = r + i, c + j
                # print(nr, nc)

                if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc ]= grid[r][c] + 1
                    # print(grid[nr][nc])
                    dq.append((nr, nc))


