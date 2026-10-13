class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #find the sum of add houses
        #find the sum of even houses

        #return max of between them

        odd = 0
        even = 0

        for i,num in enumerate(nums):
            if i%2 == 0:
                even += num
            else:
                odd += num


        return max(odd, even)