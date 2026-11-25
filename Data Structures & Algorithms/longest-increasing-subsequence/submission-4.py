class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = {}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
            
        #     if i >= len(nums):
        #         return 0
        #     res1 = 1
        #     res2 = 1

        #     for j in range(i+1, len(nums)):

        #         if nums[j] > nums[i]:
        #             print(nums[i], nums[j])
        #             print(nums[i])
        #             res1 = max(res1, 1 + dfs(j))
            
            
        #     res2 = dfs(i+1)
        #     dp[i] = max(res1, res2)
        #     return dp[i]

        
        # return dfs(0)
        
        dp = [1] * len(nums)

        for i in range(len(nums) -1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])

        
        return max(dp)

