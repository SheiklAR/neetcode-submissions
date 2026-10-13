class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        coins.sort()
        coins.reverse()

        if amount == 0:
            return 0

        ans = float('inf')

        def dfs(ind, amnt, total):
            print(coins[ind])
            print('total',total, 'amnt', amnt)
            if amnt == 0:
                return total
            

            for i in range(ind, N):
                print(amnt - coins[i], 'amnt-coins')
                if amnt - coins[i] >= 0:
                    return dfs(i, amnt-coins[i], total + 1)
            
            return -1
        

        for i in range(N):
            
            possible_coins = dfs(i, amount-coins[i], 1)
            print(possible_coins)
            if possible_coins != - 1:
                ans = min(ans, possible_coins)


            


        return  -1 if ans == float('inf') else ans