class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        d = {}
        # total_ = 0

        def dfs(i, buying):
            key = (i, buying)
            if key in d:
                return d[key]

            if i >= N:
                return 0

            if buying:
                profit = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                d[key] = max(profit, cooldown)
            else:
                profit = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                d[key] = max(profit, cooldown)
            
            return d[key]
            

        return dfs(0, True)