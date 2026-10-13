class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        # adj = {}

        ans = min(
            abs(heights[0][0] - heights[0][1]),
            abs(heights[0][0] - heights[1][0])
        )
        visit = set()

        dq = deque([(0,0)])

        while dq:
            res = float('inf')
            for _ in range(len(dq)):
                row, col = dq.popleft()

                for r,c in [(1,0), (0,1)]:
                    nr, nc = row + r, col + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        # print(nr, nc)
                        if (nr, nc) not in visit:
                            visit.add((nr, nc))
                            dq.append((nr, nc))
                        res = min(res, abs(heights[row][col] - heights[nr][nc]))
                        

            
            if not dq:
                return ans
            
            ans = max(res, ans)



        return ans