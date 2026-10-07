class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        e = equations

        adj = defaultdict(list)
        value = {}

        for i,(u,v) in enumerate(e):
            adj[u].append(v)
            adj[v].append(u)

            value[(u,v)] = values[i]
            value[(v,u)] = 1 / values[i]

        
        # print('adj ', adj)
        def dfs(product, u):
        # product *= d[(u,v)]
            if u in path:
                return -1.0
            

            if u == q[1]:
                return product
            
            path.add(u)

            for nei in adj[u]:
                res = dfs(product * value[(u, nei)], nei)
                if res  != -1.0:
                    return res
            
            path.remove(u)
            
            return -1.0
        

        ans = []

        for q in queries:
            if q[0] not in adj or q[1] not in adj:
                ans.append(-1.0)
                continue
            path = set()
            # print('query : ', q)
            ans.append(dfs(1, q[0]))
        

        return ans