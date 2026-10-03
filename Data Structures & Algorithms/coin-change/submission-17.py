class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {}

        def dfs(amnt):
            if amnt in d:
                return d[amnt]
            if amnt == 0:
                return 0
            
            ans = float('inf')
            for c in coins:
                if amnt - c >= 0:
                    res = dfs(amnt - c)
                    if res != -1:
                        ans = min(1 + res, ans)

            
            d[amnt] = -1 if ans == float('inf') else ans
            # if ans == float('inf'):
            #     d[amnt] = -1
            #     return -1
            # d[amnt] = ans
            return d[amnt]

        result = dfs(amount)
        return result

        # d = {}
        # d[0] = 0

        # coins.sort()
        

        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         if coin <= i:
        #             cur_coins = i // coin
        #             rem = i % coin

        #             if rem in d: 
        #                 cur_coins += d[rem]
        #                 if i not in d:
        #                     d[i] = float('inf')
        #                 d[i] = min(d[i], cur_coins)

        # return d.get(amount, -1)