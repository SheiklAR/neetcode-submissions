class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        r_len = len(board)
        c_len = len(board[0])

        def bt(s, r, c):
            s += board[r][c]

            if s == word:
                return True

            if len(s) == len(word):
                return False
            

            x,y,z,k = False, False, False, False
            if r + 1 < r_len:
                x = bt(s, r+1, c)
            
            if r - 1 >= 0:
                y = bt(s, r-1, c)
            
            if c + 1 < c_len:
                z = bt(s, r, c + 1)
            
            if c - 1 >= 0:
                k = bt(s, r-1, c)            

            return x or y or z or k

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if bt('', i, j):
                    return True
        

        return False
            

