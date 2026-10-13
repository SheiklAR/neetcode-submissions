class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        N = len(coins)
        coins.sort()
        coins.reverse()

        d = {}

        def dfs(start, rem_amnt):
            if rem_amnt in d:
                return d[rem_amnt]
            if rem_amnt == 0:
                return 0

            cnt = float('inf')
            for i in range(start, N):
                if not rem_amnt < coins[i]:
                    res = dfs(i, rem_amnt - coins[i])
                    if res != - 1:
                        cnt = min(cnt, res + 1)


            if cnt == float('inf'):
                d[rem_amnt] = -1
                return -1
            else:
                d[rem_amnt] = cnt
                return cnt


        dfs(0, amount)
        return d.get(amount, -1)