class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        WORD = len(word)

        rec_stack = set()

        def bt(s, r, c, i):
            print(s, r, c, i)
            print(rec_stack)
            if (
                r >= ROWS or r < 0 or
                c >= COLS or c < 0 or
                board[r][c] != word[i] or
                (r, c) in rec_stack
            ):
                return False

            if i == WORD - 1:
                return True
            
            rec_stack.add((r, c))

            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if bt(s, r + di, c + dj, i+1):
                    return True

            rec_stack.remove((r, c))
            return False
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if bt('', i, j, 0):
                    return True
        

        return False
            

