class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        ans = []

        def bt(arr, ind):

            sum_ = sum(arr)

            if sum_ == target:
                ans.append(arr[:])
                return

            if sum_ > target:
                return

            for i in range(ind, n):
                arr.append(nums[i])
                bt(arr, i)
                arr.pop()
         

        bt([], 0)
        return ans
