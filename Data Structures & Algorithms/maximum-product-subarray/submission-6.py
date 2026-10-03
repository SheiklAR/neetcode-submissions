class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        global_pro, cur_pro, last_neg = 1, 1, 1

        for num in nums:
            
            global_pro *= num
            cur_pro *= num
            last_neg *= num

            ans = max(ans, global_pro, cur_pro, num)

            if num < 0:
                #reset
                cur_pro = max(last_neg, 1)
                last_neg = num

        return ans