import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        #create the empty board
        board = [['.'] * n for _ in range(n)]
        
        ans = []

        #check by putting values in each row


        #each step check for conflict
        def verify_conflict(row, col):
            #check cols of the prevs
            r = row - 1
            while r >= 0:
                if board[r][col] == 'Q':
                    return True
                r -= 1

            #check top right diagnol
            r = row - 1
            c = col + 1
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return True
                r -= 1
                c += 1
            
            #check top left diagnol
            r = row - 1
            c = col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return True
                r -= 1
                c -= 1


            return False


        #add dirs for each

        def bt(r):
            if r >= n:
                ans.append(copy.deepcopy(board))

            for c in range(n):
                if verify_conflict(r, c) == False:
                    board[r][c] = 'Q'
                    bt(r+1)
                    board[r][c] = '.'
        
        bt(0)
        result = []

        for i in range(len(ans)):
            cur = ["".join(row) for row in ans[i]]
            result.append(cur)

        return result

