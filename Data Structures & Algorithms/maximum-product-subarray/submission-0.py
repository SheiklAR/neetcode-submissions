class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        #1-n size

        #optimize the window start with window 1 and to len(nums)
        ans = float('-inf')
        cur_product, global_product = 1, 1

        for num in nums:
            # third = num
            # if num < 0:
            #     if cur_product < 0:
            #         cur_product *= num
            # else:
            #     cur_product = 1
            
            cur_product *= num
            global_product *= num

            ans = max(global_product, cur_product, num)

            if num < 0 and cur_product < 0:
                #reset
                cur_product = 1

    
        return ans