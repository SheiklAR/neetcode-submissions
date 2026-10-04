class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        visited = set()
        adj = defaultdict(set)

        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)



        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if node in adj[nei]:
                        adj[nei].remove(node)
                        dfs(nei)
        
        
        for u in range(n):
            if u not in visited:
                cnt += 1
                dfs(u)
        
        return cnt