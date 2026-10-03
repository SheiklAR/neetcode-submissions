class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        cache = {}
        
        def dfs(i, t):
            key = (i, t)
            if key in cache:
                return cache[key]
            if i == N and t == target:
                return 1
            if i >= N:
                return 0
            
            res = dfs(i+1, t+nums[i]) + dfs(i+1, t - nums[i])
            cache[key]  = res

            return cache[key]


        return dfs(0,0)