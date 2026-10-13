class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {}
        d[0] = 0

        #5  // 2
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    cur_coins = i // coin #1
                    rem = i % coin #0

                    if rem in d: 
                        cur_coins += d[rem]
                        if i not in d:
                            d[i] = float('inf')
                        d[i] = min(d[i], cur_coins)
                

        return d.get(amount, -1)