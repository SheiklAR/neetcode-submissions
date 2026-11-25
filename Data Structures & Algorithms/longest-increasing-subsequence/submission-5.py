class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            
    
            res1 = 1

            for j in range(i+1, len(nums)):

                if nums[j] > nums[i]:
                    # print(nums[i], nums[j])
                    # print(nums[i])
                    res1 = max(res1, 1 + dfs(j))
            
            
            # res2 = dfs(i+1)
            dp[i] = res1
            return dp[i]

        
        # return dfs(0)

        
        
        return max(dfs(i) for i in range(len(nums)))
        
        # dp = [1] * len(nums)

        # for i in range(len(nums) -1, -1, -1):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] > nums[i]:
        #             dp[i] = max(1 + dp[j], dp[i])

        
        # return max(dp)

