class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def bt(arr,i):
            n = len(nums)
            res.append(arr[:])

            if i > n-1:
                return

            for j in range(i, n):
                arr.append(nums[j])
                bt(arr, j+1)
                arr.pop()


        bt([], 0)
        return res

