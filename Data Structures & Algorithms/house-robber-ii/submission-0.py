class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 6 2 9 8 3 6
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        hasLast = [False] * n
        ans = [0] * (n + 2)

        hasLast[n-1] = True

        for i in range(n-1, 0, -1):
            nei = i+1
            next_ = i+2

            if i+1 >= n or i+2 >= n:
                print(ans[i])
                ans[i] = nums[i]
            else:
                cur_val1 = nums[i] + nums[next_]
                cur_val2 = nums[i] + ans[nei] - nums[nei]

                if cur_val1 > cur_val2:
                    hasLast[i] = hasLast[next_]
                    ans[i] = cur_val1

                elif cur_val2 > cur_val1:
                    hasLast[i] = hasLast[nei]
                    ans[i] = cur_val2
                else:
                    hasLast[i] = hasLast[nei] or hasLast[next_]
                    ans[i] = cur_val1
        
        print(ans)
        i = 0
        nei = ans[i+1] - nums[i] - nums[n-1] if hasLast[i+1] else ans[i+1] - nums[i]
        next_ = ans[i+2] - nums[n-1] if hasLast[i+2] else ans[i+2]

        ans[0] = max(nums[0], nums[0] + nei, nums[0]+ next_)

        return max(ans[0], ans[1])