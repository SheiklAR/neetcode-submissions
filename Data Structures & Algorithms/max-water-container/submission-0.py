class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i, j = 0, len(heights) - 1

        water_level = 0

        while i < j:
            hi, hj = heights[i], heights[j]
            water_level = max(water_level, min(hi, hj) * (j - i))

            if hi < hj:
                i += 1
            else:
                j -= 1
        
        return water_level

