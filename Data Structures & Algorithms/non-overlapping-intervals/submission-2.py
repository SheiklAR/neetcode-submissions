class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = [intervals[0]] # [1, 3], [2, 4]

        for i in intervals[1:]:
            if ans[-1][-1] > i[0]:
                if (ans[-1][-1] - ans[-1][0]) > (i[1] - i[0]):
                    ans.pop()
                    ans.append(i)
                elif (ans[-1][-1] - ans[-1][0]) == (i[1] - i[0]):
                    if i[1] < ans[-1][-1]:
                        ans.pop()
                        ans.append(i)
            else:
                ans.append(i)

                
        # print(ans)
        return len(intervals) - len(ans)