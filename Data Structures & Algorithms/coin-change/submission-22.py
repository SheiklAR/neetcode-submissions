class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        [1, 2, 2]

        if amount == 0:
            return 0

        # min denm = 1

        # 4 => amount

        # if is in dp then return dp[amnt]

        # else go through coins 1 +

        dp = {}
        # dp[0] = 0

        def dfs(amnt):
            if amnt == 0:
                return 0
            if amnt in dp:
                return dp[amnt]
            
            if amnt < 0:
                return float('inf')

            # print('here')
            res = float('inf')
            # print('here')
            for coin in coins:
                # print(amnt-coin)
                res2 = dfs(amnt-coin)
                if res2 != float('inf'):
                    res = min(1 + res2, res)

            
            dp[amnt] = res
            # print(amnt, res)
            return dp[amnt]
    

        


        for a in range(1, amount + 1):
            res = float('inf')
            # print('a', a)
            for coin in coins:
                # print(a-coin)
                res =  min(1 + dfs(a-coin), res)
            
            dp[a] = res
            # print('amnt', a, 'res', res)

        # print(dp)
        return -1 if dp[amount] == float('inf') else dp[amount]