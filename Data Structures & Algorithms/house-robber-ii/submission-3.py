class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 6 2 9 8 3 6
        n = len(nums)
        if n == 1:
            return nums[0]


        def maxCost(arr):
            #optimized bottom-up
            n = len(arr)
            if n == 1:
                return arr[0]

            next_ = arr[0]
            prev = arr[1]
            cur = 0

            for i in range(2, n):
                cur = max(arr[i] + next_, arr[i] + prev - arr[i-1])
                print(cur)
                next_ = prev
                prev = cur
            
            return max(prev, next_)


        return max(maxCost(nums[:n-1]), maxCost(nums[1:]))