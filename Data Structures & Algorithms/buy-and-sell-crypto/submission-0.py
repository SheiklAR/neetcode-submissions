class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        hpc = None

        for p in prices:
            if hpc == None:
                hpc = p
                continue
            if p > hpc:
                ans = max(ans, p-hpc)
            else:
                hpc = p
        
        return ans