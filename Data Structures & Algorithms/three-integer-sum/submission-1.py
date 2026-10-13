class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        # [-4, -1, -1, 0, 1, 2]
        # [-1, -1, 0, 1, 2]

        # -1 -1 + 2 = 1
        ans = []

        prev = None
        for n in range(len(nums)):
            if prev == nums[n]:
                print('here')
                continue
            i,j = n+1, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + nums[n] == 0: 
                    ans.append([nums[n], nums[i], nums[j]])
                    j -= 1
                
                else:
                    if nums[i] + nums[j] + nums[n] < 0:
                        i += 1
                    else:
                        j -= 1
            prev = nums[n]
        return ans
                


