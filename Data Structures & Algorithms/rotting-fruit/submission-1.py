class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        mins = 0
        dq = deque([])


        for r in range(ROWS):
            for c in range(COLS):
                # count fresh
                if grid[r][c] == 1:
                    fresh += 1
                # put rotten in a deque
                if grid[r][c] == 2:
                    dq.append((r, c))

        # print(dq)
        if fresh == 0: return 0
        cnt = 0

        while dq:
            flag = False
            for _ in range(len(dq)):
                # pop
                r,c = dq.popleft()

                # change neighbours
                for i,j in dirs:
                    nr, nc = r+i, c+j

                    if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            dq.append((nr, nc))
                            flag = True
                            cnt += 1
            if flag: 
                mins += 1 

            

        # print(mins)
        return mins if cnt == fresh else -1