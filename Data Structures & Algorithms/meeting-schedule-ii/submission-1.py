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
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()

        cnt = 0
        s, e = 0, 0

        while s < len(start):
            if end[e] <= start[s]:
                e += 1
                s += 1
                continue
            cnt += 1
            s += 1
            
        
        return cnt


