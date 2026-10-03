class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dq = deque([])
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dq.append((r, c))
                    visit.add((r, c))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        val = 1

        while dq:
            n = len(dq)
            for _ in range(n):
                row, col = dq.popleft()

                for r,c in dirs:
                    nr, nc = row + r, col + c

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] > -1 and
                        (nr, nc) not in visit
                    ):
                        grid[nr][nc] = val
                        visit.add((nr, nc))
                        dq.append((nr, nc))
            
            val += 1


        # ROWS, COLS = len(grid), len(grid[0])
        
        # # heap = [(0, r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 0 ]
        # dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # if heap:
        #     visit = set((heap[0][1], heap[0][1]))


        # while heap:
        #     val, row, col = heappop(heap)

        #     for r,c in dirs:
        #         nr, nc = row + r, col + c

        #         if 0 <= nr < ROWS and 0 <= nc < COLS and val > -1:
        #             grid[nr][nc] = min(grid[nr][nc], 1 + val)

        #             if (nr, nc) not in visit:
        #                 visit.add((nr, nc))
        #                 heappush(heap, (grid[nr][nc], nr, nc))
        #     for r,c in dirs:
        #         nr, nc = row + r, col + c

        #         if 0 <= nr < ROWS and 0 <= nc < COLS and val > -1:
        #             grid[nr][nc] = min(grid[nr][nc], 1 + val)

        #             if (nr, nc) not in visit:
        #                 visit.add((nr, nc))
        #                 heappush(heap, (grid[nr][nc], nr, nc))



        
        