class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def bt(arr):
            # print(arr)
            if len(arr) == len(nums):
                ans.append(arr[:])

            for num in nums:
                if num not in arr:
                    arr.append(num)
                    bt(arr)
                    arr.pop()
        
        bt([])


        return ans