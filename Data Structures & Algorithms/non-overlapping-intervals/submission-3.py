class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0] # [1, 3], [2, 4]
        cnt = 0


        for cur in intervals[1:]:
            if prev[-1] > cur[0]:
                cnt += 1
                if prev[1] > cur[1]:
                    prev = cur
            else:
                prev = cur

                
        # print(ans)
        return cnt