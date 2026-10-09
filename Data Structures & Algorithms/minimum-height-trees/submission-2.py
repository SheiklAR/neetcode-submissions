class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        
        adj = defaultdict(set)

        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        dq = deque([])
        visit = set()

        for key,val in adj.items():
            if len(val) == 1:
                dq.append(key)
                visit.add(key)
        
        print(dq)
        cnt = n

        while cnt > 2:

            for _ in range(len(dq)):
                node = dq.popleft()
                cnt -= 1
                for nei in adj[node]:
                    adj[nei].remove(node)
                    if nei not in visit and len(adj[nei]) <= 1:
                        dq.append(nei)
                        visit.add(nei)
            


        return list(dq)