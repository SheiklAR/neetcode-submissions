class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        #bottom up approach
        # ans = [0] * (len(nums) + 2)

        next_ = nums[0]
        prev = nums[1]
        cur = 0

        for i in range(2, n):
            cur = max(nums[i] + next_, nums[i] + prev - nums[i-1])
            print(cur)
            next_ = prev
            prev = cur
            
        
        return max(prev, next_)




        
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
            
