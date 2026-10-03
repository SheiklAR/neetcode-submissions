class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        d = {}

        nums = [1] + nums + [1]


        def dfs(l, r):
            key = (l,r)
            if key in d:
                return d[key]

            if l < 1 or r > len(nums) - 1:
                return 0

            res = 0
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                res = max(res, coins + dfs(l,i-1) + dfs(i+1, r))
                
            d[key] = res
            return res
        
        return dfs(1, len(nums) - 2)