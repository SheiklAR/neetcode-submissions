class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        
        # if ROWS == COLS == 1:
        #     return 0

        
        def dfs(row, col, k):
            print(row, col, k)
            if (row, col) == (ROWS - 1, COLS - 1):
                # print('here')
                return True

            
            visit.add((row, col))
            for r,c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                nr, nc = row + r, col + c

                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS:
                    if (nr, nc) not in visit and abs(heights[nr][nc] - heights[row][col]) <= k:    
                        # print('nr, nc', nr, nc, h[nr][nc], h[r][c])
                        # print(abs(heights[nr][nc] - heights[r][c]))
                        if dfs(nr, nc, k):
                            return True
                

            return False



        values = set()
        h = heights

        for r in range(ROWS-1):
            for c in range(COLS-1):
                values.add(abs(h[r + 1][c]-h[r][c]))
                values.add(abs(h[r][c + 1]-h[r][c]))
                
        
        values = list(values)


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
        
        return ans

                




