class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        N = len(coins)
        coins.sort()
        coins.reverse()

        d = defaultdict(lambda : -1)

        def dfs(start, rem_amnt):
            if rem_amnt == 0:
                return 0

            cnt = float('inf')
            for i in range(start, N):
                if not coins[i] > rem_amnt:
                   res = dfs(i, rem_amnt - coins[i])
                   if res != - 1:
                        cnt = min(cnt, res + 1)
                     
            if cnt == float('inf'):
                return -1
            else:
                d[rem_amnt] = cnt
                return cnt


        dfs(0, amount)
        return d[amount]