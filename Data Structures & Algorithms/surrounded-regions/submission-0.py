class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def mark_safe(i, j):

            board[i][j] = '#'

            for r, c in dirs:
                nr, nc = r + i, c + j


                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    board[nr][nc] == 'O'
                ):
                    mark_safe(nr, nc)

            return
        
        
        # Top edge
        for c in range(COLS):
            if board[0][c] == 'O':
                mark_safe(0, c)

        # left edge
        for r in range(ROWS):
            if board[r][0] == 'O':
                mark_safe(r, 0)
        

        # right edge
        for r in range(ROWS):
            if board[r][COLS-1] == 'O':
                mark_safe(r, COLS-1)
        
        # bottom edge
        for c in range(COLS):
            if board[ROWS-1][c] == 'O':
                mark_safe(ROWS-1, c)
        

        # reverse back O and capture regions
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == '#':
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"