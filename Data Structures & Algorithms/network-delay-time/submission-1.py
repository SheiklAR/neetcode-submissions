from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v, w))
        
        min_heap = [(0, k)]

        visited = set()
        weight = defaultdict(lambda : float('inf'))
        weight[k] = 0


        visited.add(k)
        while min_heap:
            w,u = heappop(min_heap)

            for v,wei in adj[u]:
                if weight[v] > w + wei:
                    weight[v] = min(weight[v], w + wei)
                    heappush(min_heap, ((weight[v]),v))
                    visited.add(v)

        
        if len(visited) < n:
            return -1
        else:
            return max(weight.values())