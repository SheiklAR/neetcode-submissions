class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        ans = []

        def bt(arr, ind):
            ans.append(arr[:])
            print(arr[:])

            if ind == n:
                return


            while ind < n:
                arr.append(nums[ind])
                bt(arr, ind + 1)
                arr.pop()

                while ind +  1 < n and nums[ind] == nums[ind+1]:
                    ind += 1
                
                ind += 1
        
        bt([], 0)

        return ans


            
                
