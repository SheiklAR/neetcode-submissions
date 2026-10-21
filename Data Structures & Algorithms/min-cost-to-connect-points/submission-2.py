class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, N):
               
                x2, y2 = points[j][0], points[j][1]
                c = abs(x1-x2) + abs(y1-y2)
                adj[i].append((c, j))
                adj[j].append((c, i))

        # print(adj)
        ans = 0
        heap = [(0, 0)]
        visit = set()


        while heap:
            # print('here')
            cost, node = heapq.heappop(heap)
            if node in visit:
                continue
            
            visit.add(node)
            ans += cost



            
            for cost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(heap, (cost, nei))
                    # visit.add(nei)


        return ans