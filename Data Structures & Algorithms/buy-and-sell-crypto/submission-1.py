class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        hi_profit_coin = None

        for p in prices:
            if hi_profit_coin == None:
                hi_profit_coin = p
                continue
            if p > hi_profit_coin:
                ans = max(ans, p-hi_profit_coin)
            else:
                hi_profit_coin = p
        
        return ans