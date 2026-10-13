class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        visited = set()

        for u,v,w in times:
            adj[u].append((v, w))
        
        # print(adj)
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, k))
        
        ans = -1

        while minHeap:

            w, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            ans = max(ans, w)
            visited.add(node)

            print(adj[node])

            for nei, nw in adj[node]:
                
                if nei not in visited:
                    heapq.heappush(minHeap, ((w + nw), nei))

        
        print(visited)
        if len(visited) == n:
            return ans
        
        return -1
            