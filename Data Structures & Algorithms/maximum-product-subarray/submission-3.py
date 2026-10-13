class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur_product, global_product, last_negative = 1, 1, 1

        for num in nums:
            # third = num
            # if num < 0:
            #     if cur_product < 0:
            #         cur_product *= num
            # else:
            #     cur_product = 1


            
            cur_product *= num
            global_product *= num
            last_negative *= num



            ans = max(ans, global_product, cur_product, num)

            if num < 0:
                if last_negative > 0:
                    cur_product = last_negative
                else:
                    last_negative = num
                    cur_product = 1

    
        return ans