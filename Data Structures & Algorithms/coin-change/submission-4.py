class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort()
        
        ROWS = len(coins)
        COLS = amount

        dp = [[-1] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS+1):
            dp[r][0] = 0
        
        for r in range(ROWS):
            coin = coins[r]
            row = r + 1
            print("coin", coin)
            for c in range(COLS):
                col = c + 1
                amnt = c + 1
                print(amnt)
                # print(dp[row-1][col])

                if coin > amnt:
                    dp[row][col] = dp[row-1][col]
                
                else:
                    res = amnt // coin
                    rem = amnt % coin

                    dp[row][col] = -1 if dp[row][rem] == -1 else res + dp[row][rem]
                

        print(dp)
        return dp[-1][-1]
            
