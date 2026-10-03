class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        second_last = 0 
        last = 1
        cur = 2

        for i in range(3, n+1):
            second_last, last = last, cur
            cur = last + second_last
        
        return cur
        