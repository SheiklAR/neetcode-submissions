class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def dfs(ind):
            if ind == n - 1:
                cache[ind] = 1
                return
            
            dfs(ind+1)
            if ind + 1 in cache:                
                print('here')
                cache[ind] = cache[ind+1] + 1 if nums[ind] < nums[ind+1] else cache[ind+1]
                print(cache)

        dfs(0)
        return cache[0]