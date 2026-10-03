class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        second_last = 0 #1,2, 3 ||2,3, 5 || 3,5 8
        last = 1
        
        cur = 2
        for i in range(3, n+1):
            second_last, last = last, cur
            print(second_last, last)
            cur = last + second_last
        
        return cur
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        if n == 4:
            return 5
        
        if n == 5:
            return 8
        
        if n == 6:
            return 13
        
        if n == 7:
            return 21
        
        if n == 8:
            return 34
        #1 - 1
        #2 - 1+1, 2
        #3 - 1+1+1, 2+1, 1+2 3
        #4 - 4X1, 2X2, 112, 211 4
        #5 = 8
        #

        return 0