class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        r_len = len(board)
        c_len = len(board[0])

        rec_stack = set()

        def bt(s, r, c):
            print('r, c : ', r, c)
            if (r,c) in rec_stack:
                return False
            
            rec_stack.add((r, c))

            if r >= r_len or r < 0 or c >= c_len or c < 0:
                return False
                
            print(rec_stack)

            
            s += board[r][c]

            if s != word[:len(s)]:
                return False
            
            print(s, word[:len(s)])
            if s == word: return True


            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if bt(s, r + i, c + j):
                    return True
                rec_stack.remove((r + i, c + j))
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if bt('', i, j):
                    return True
        

        return False
            

