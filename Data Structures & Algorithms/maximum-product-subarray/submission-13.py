class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negative_cnt = 0
        total, positive = 1, 1
        ans = float('-inf')
        first_negative = -1

        

        for num in nums: # 4, -2, 3, 1

            total = num * total
            positive = num * positive

            if num == 0:
                total, positive = 1, 1
                negative_cnt = 0
                ans = max(num, ans)
                continue
            
            if num < 0:
                positive = 1
                negative_cnt += 1

                if negative_cnt == 1:
                    first_negative = total

                if negative_cnt > 2:
                    ans = max(ans, num, total, positive, int(total / first_negative))
                else:
                    ans = max(ans, num, total)
                positive = 1

                
            else:
                ans = max(ans, positive, total, int(total/first_negative))
                
        

        return ans

