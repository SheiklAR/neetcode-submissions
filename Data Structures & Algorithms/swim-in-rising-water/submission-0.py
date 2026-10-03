from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        heap = [(grid[0][0], 0, 0)] 
        # d = {(0, 0): grid[0][0]} #new version


        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while heap:
            v, r, c = heappop(heap)
            # print(v)

            # new version
            if (r, c) in visited:
                continue

            visited.add((r, c))



            # new version
            if r == ROWS - 1 and c == COLS - 1:
                return v

            for row, col in dirs:
                nr, nc = row + r, col + c

                # if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in d or (nr, nc) in visited:
                #     continue # new version

                # new version
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                    continue # new version

                val = max(v, grid[nr][nc]) # tricky part or should observer carefully

                # if (nr, nc) not in d:
                heappush(heap, (val, nr, nc))
                # d[(nr, nc)] = float('-inf')

                # d[(nr, nc)] = max(d[(nr,nc)], val)
            
        
        return d[(ROWS - 1, COLS - 1)]