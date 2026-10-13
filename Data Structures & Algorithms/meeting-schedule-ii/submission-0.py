"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if not intervals:
        #     return 0
        # 0 -> 40, 5 - 10, 15 - 20

        # 0 -> 40
        intervals.sort(key=lambda x: x.start)
        cnt = 0

        for i,cur in enumerate(intervals):
            if i == 0:
                cnt += 1
            else:
                prev = intervals[i-1]
                if prev.end > cur.start:
                    cnt += 1
                
        
        return cnt


