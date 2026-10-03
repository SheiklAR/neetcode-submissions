class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        
        def dfs(i, t):
            if i == N and t == target:
                return 1
            if i >= N:
                return 0
            
            return dfs(i+1, t+nums[i]) + dfs(i+1, t - nums[i])


        return dfs(0,0)