class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dq = deque([])
        visit = set()

        non_rotten = 0
        rotten = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visit.add((r, c))
                    dq.append((r, c))
                    rotten += 1
                elif grid[r][c] == 1:
                    non_rotten += 1

        mins = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            n = len(dq)

            for _ in range(n):
                row, col = dq.popleft()

                for r,c in dirs:
                    nr, nc = row + r, col + c

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visit and
                        grid[nr][nc] == 1
                    ):
                        # print((nr, nc))
                        # grid[nr][nc] = 2
                        visit.add((nr, nc))
                        dq.append((nr, nc))
            if dq:
                mins += 1
        
        
        # print(non_rotten, rotten, len(visit))
        return mins if non_rotten + rotten == len(visit) else -1