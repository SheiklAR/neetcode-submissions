class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        

        #1 - 1
        #2 - 1+1, 2
        #3 - 1+1+1, 2+1, 112
        #4 - 4X1, 2X2, 112, 121

        return (n-1) + (n-2)