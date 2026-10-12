class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        print(ROWS, COLS)
        
        # if ROWS == COLS == 1:
        #     return 0

        
        def dfs(row, col, k):
            stack = []
            stack.append((row, col))
            
            while stack:
                row, col = stack.pop()

                if (row, col) == (ROWS - 1, COLS - 1):
                    return True
                for r,c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                    nr, nc = row + r, col + c

                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS:
                        if (nr, nc) not in visit and abs(heights[nr][nc] - heights[row][col]) <= k:    
                            stack.append((nr, nc))
                            visit.add((nr, nc))
                

            return False



        values = set()
        h = heights

        for r in range(ROWS):
            for c in range(COLS):
                if r + 1 < ROWS:
                    values.add(abs(h[r + 1][c]-h[r][c]))
                if c + 1 < COLS:
                    values.add(abs(h[r][c + 1]-h[r][c]))
                
        
        values = sorted(list(values))


        l, r = 0, len(values) - 1
        ans = float('inf')
        # visit = set()
        # dfs(0, 0, 4)
        # return 0
        while l <= r:

            m = (l + r) // 2
            visit = set((0, 0))
            if not dfs(0, 0, values[m]):
                l = m + 1
            else:
                ans = min(ans, values[m])
                r = m - 1
        
        return ans if ans != float('inf') else 0

                




