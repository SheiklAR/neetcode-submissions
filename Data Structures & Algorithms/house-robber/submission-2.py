class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #find the sum of add houses
        #find the sum of even houses
        #return max of between them

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
            
