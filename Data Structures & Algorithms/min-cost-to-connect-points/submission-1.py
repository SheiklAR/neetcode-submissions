from heapq import heappush, heappop

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        heap = [(0, 0)]
        cnt = 0
        ans = 0

        while cnt < len(points):
            w,u = heappop(heap)

            if u in visited:
                continue
            
            visited.add(u)
            ans += w
            cnt += 1

            x1, y1 = points[u][0], points[u][1]
            for v in range(len(points)):
                if v not in visited:
                    x2, y2 = points[v][0], points[v][1]
                    val = abs(x1 - x2) + abs(y1 - y2)
                    heappush(heap, (val, v))

        
        return ans