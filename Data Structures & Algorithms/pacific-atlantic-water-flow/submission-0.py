class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        # visit = set()
        pacific_set = set() 
        atlantic_set = set()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i,j,prev,ocean):
            for r, c in dirs:
                nr, nc = i + r, c + j

                if (
                    0 <= nr < ROWS and 0 <= nc < COLS and
                    heights[nr][nc] >= prev
                    # (nr, nc) not in visit and
                ):
                    if ocean == 'pacific':
                        if (nr, nc) not in pacific_set:
                            pacific_set.add((nr, nc))
                            dfs(nr, nc, heights[nr][nc], ocean)
                    else:
                        if (nr, nc) not in atlantic_set:
                            atlantic_set.add((nr, nc))
                            dfs(nr, nc, heights[nr][nc], ocean)

            return
        

        #pacific
        for c in range(COLS):
            # pacific_set.add((0, c))
            if (0, c) not in pacific_set:
                pacific_set.add((0, c))
                dfs(0, c, heights[0][c], 'pacific')
        for r in range(ROWS):
            # pacific_set.add((r, 0))
            if (r, 0) not in pacific_set:
                pacific_set.add((r, 0))
                dfs(r, 0, heights[r][0], 'pacific')


        #atlantic
        for c in range(COLS):
            # atlantic_set.add((ROWS-1, c))
            if (ROWS-1, c) not in atlantic_set:
                atlantic_set.add((ROWS-1, c))
                dfs(ROWS-1, c, heights[ROWS-1][c], 'atlantic')
        for r in range(ROWS):
            # atlantic_set.add((r, COLS-1))
            if (r, COLS-1) not in atlantic_set:
                atlantic_set.add((r, COLS-1))
                dfs(r, COLS-1, heights[r][COLS-1], 'atlantic')

        

        ans = []

        # print(pacific_set)
        # print(atlantic_set)

        for x in pacific_set:
            if x in atlantic_set:
                ans.append(list(x))
        
        return ans