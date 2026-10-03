class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        

        
        # 1 4 7 -> 7 4 1
        # 2 5 8 -> 2 5 8
        # 3 6 9 -> 9 6 3
        # pattern
        # 1st row second col
        # 2nd row third col

        for r in range(ROWS):
            for c in range(r+1, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for row in matrix:
            row.reverse()