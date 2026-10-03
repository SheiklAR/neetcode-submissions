class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #find the sum of add houses
        #find the sum of even houses
        #return max of between them

        ans = [0] * (len(nums) + 2)

        for i in range(len(nums)-1, -1, -1):
            nei = ans[i+1]
            next_ = ans[i+2]

            if i + 1 >= len(nums) or i + 2 >= len(nums):
                ans[i] = nums[i]
            else:
                ans[i] = max(nums[i] + next_, nums[i] + (nei - nums[i+1]))
        
        
        print(ans)
        return ans[0] if len(ans) == 1 else max(ans[0], ans[1])


        
        '''
        *memoization*
        cache = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]
            
            nei = dfs(i+1)
            next_ = dfs(i+2)

            if i+1 >= len(nums):
                cur_max = nums[i] + next_
            else:
                cur_max = max(nums[i]+next_, nums[i] + (nei - nums[i+1]))

            cache[i] = cur_max

            return cur_max

        return max(dfs(0), dfs(1))
        '''
            
