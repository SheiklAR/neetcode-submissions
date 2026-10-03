class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #right---> down ---> left ---> up --> right
        ROWS, COLS = len(matrix), len(matrix[0])

        ans = []
        
        left = (0,-1)
        down = (1,0)
        up = (-1,0)
        right = (0,1)

        def get_spiral_order(dirn, r, c):
            if len(ans) == ROWS * COLS:
                return
            # r, c = dirn[0], dirn[1]
            dirn = dirn

            while 0 <= r < ROWS and 0 <= c < COLS and matrix[r][c] < 101:
                ans.append(matrix[r][c])
                matrix[r][c] = 101
                r,c = r + dirn[0], c + dirn[1]
            

            r, c = r - dirn[0], c - dirn[1]
            print(r,c)
            if dirn == right:
                get_spiral_order(down, r + down[0], c + down[1])
            
            if dirn == down:
                get_spiral_order(left, r + left[0], c + left[1])

            if dirn == left:
                get_spiral_order(up, r + up[0], c + up[1])
            
            
            if dirn == up:
                get_spiral_order(right,r + right[0], c + right[1])


        get_spiral_order(right, 0, 0)
        return ans