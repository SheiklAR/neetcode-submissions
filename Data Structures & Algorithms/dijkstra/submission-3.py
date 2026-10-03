from heapq import *
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # adj list, 
        # implementation -> using min heap -> 
        # needed min weight -> process min weight first
        # relax edges. # min(weight, newweight)
        adj = defaultdict(list)
        for s,d,wei in edges:
            adj[s].append([d, wei])
        
        ans = {src:0}
        min_heap = []

        for d,we in adj[src]:
            heappush(min_heap, (we, d))
            ans[d] = we

        
        while min_heap:
            we, e = heappop(min_heap)

            # if e in adj:
            for d,wei in adj[e]:
                if d not in ans:
                    heappush(min_heap, (ans[e] + wei, d))
                    # if d not in ans:
                    ans[d] = ans[e] + wei
                else:
                    ans[d] = min(ans[d], ans[e] + wei)
        
        for i in range(n):
            if i not in ans:
                ans[i] = -1
        
        return ans









