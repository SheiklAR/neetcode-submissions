class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        processed = 0
        adj = defaultdict(set)
        visited = set()
        path = set()

        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)


        def dfs(node):
            # nonlocal processed
            if node in path:
                return False
            
            path.add(node)

            if node in visited:
                return True

            visited.add(node)

            # processed += 1


            for nei in adj[node]:
                if node in adj[nei]:
                    adj[nei].remove(node)
                if not dfs(nei):
                    return False
            
            path.remove(node)
            return True
        

        # print(adj)
        if dfs(0) and len(visited) == n:
            return True
        
        
        # print(visited)
        return False
            
