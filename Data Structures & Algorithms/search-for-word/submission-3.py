class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        r_len = len(board)
        c_len = len(board[0])

        def bt(s, r, c):
            s += board[r][c]

            if s == word:
                print(s)
                return True

            if len(s) == len(word):
                return False
            
            set_.add((r, c))

            x,y,z,k = False, False, False, False
            if r + 1 < r_len and (r+1, c) not in set_:
                x = bt(s, r+1, c)
            
            if r - 1 >= 0 and (r-1, c) not in set_:
                y = bt(s, r-1, c)
            
            if c + 1 < c_len and (r, c+1) not in set_:
                z = bt(s, r, c + 1)
            
            if c - 1 >= 0 and (r, c-1) not in set_:
                k = bt(s, r, c - 1)            

            return x or y or z or k

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                set_ = set()
                if bt('', i, j):
                    return True
        

        return False
            

