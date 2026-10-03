from heapq import heappop, heappush
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        d = {}
        ans = float('inf')

        for s,d,c in flights:
            adj[s].append((d, c))
        
        visited = set()
        min_heap = [(0, -1, src)]
        d = {(src, -1): 0}

        ans = float('inf')

        while min_heap:
            # print('here')
            c,cnt,u = heappop(min_heap)

            if d[(u,cnt)] > c:
                continue

            # visited.add((u, cnt))

            if u == dst:
                # print('cost', c, cnt)
                ans = min(ans, c)
            
            for v,c2 in adj[u]:
                if cnt + 1 <= k:
                    # print(cnt + 1)
                    # if v not in d:
                    #     d[v] = [float('inf'), float('inf')]

                    if (v, cnt + 1) not in d:
                        d[(v, cnt + 1)] = c + c2
                        heappush(min_heap, (d[(v, cnt + 1)], cnt + 1, v))
                    else:
                        if d[(v, cnt+1)] > c + c2:
                            d[(v, cnt + 1)] = c + c2
                            heappush(min_heap, (d[(v, cnt + 1)], cnt + 1, v))
        
        
        return - 1 if ans == float('inf') else ans