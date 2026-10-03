from heapq import *
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        d = {q:i for i,q in enumerate(queries)}
        ans = {}
        intervals.sort()
        qs = [q for q in queries]
        queries.sort()

        min_heap = []
        ans = []

        i = 0
        for q in queries:
            # print(q)
            while i < len(intervals):
                s,e = intervals[i]
                if s <= q:
                    heappush(min_heap, (e - s + 1, e))
                    i += 1
                else:
                    break
            # print(min_heap)
            

            while min_heap:
                if not min_heap[0][1] >= q:
                    heappop(min_heap)
                else:
                    break

            if not min_heap:
                d[q] = -1
                # print(d[q])
            else:
                d[q] = min_heap[0][0]


        res = []

        for q in qs:
            res.append(d[q])


        return res