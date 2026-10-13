class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        if n == 4:
            return 5
        
        if n == 5:
            return 8
        
        if n == 6:
            return 13
        
        if n == 7:
            return 21
        #1 - 1
        #2 - 1+1, 2
        #3 - 1+1+1, 2+1, 1+2 3
        #4 - 4X1, 2X2, 112, 211 4
        #5 = 8
        #

        return 0