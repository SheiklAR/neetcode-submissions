class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def dfs(ind):
            if ind in cache:
                return cache[ind]
            
            ans = float('-inf')
            for j in range(ind+1, n):
                if nums[ind] < nums[j]:
                    ans = max(dfs(j), ans)
            
            if ans == float('-inf'):
                cache[ind] = 1
                return 1
            else:
                cache[ind] = 1 + ans
                return 1 + ans
            

        for i in range(n):
            dfs(i)

        print(cache)
        return max(cache.values())