class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        prefix = 1
        suffix = 1

        #prefix
        for num in nums:
            prefix *= num
            ans = max(ans, prefix, num)

            if prefix == 0:
                prefix = 1

        #suffix
        for num in reversed(nums):
            suffix *= num
            ans = max(ans, suffix, num)

            if suffix == 0:
                suffix = 1
        
        return ans