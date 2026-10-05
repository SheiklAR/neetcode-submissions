class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = defaultdict(set)

        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        def dfs(node):
            nonlocal cnt
            if node in visited:
                return True
            
            if node in path:
                return False
            
            path.add(node)
            visited.add(node)
            cnt += 1


            for nei in adj[node]:
                if not dfs(nei):
                    print(path)
                    return False
            
            path.remove(node)
            return True
        

        for u,v in reversed(edges):
            adj[u].remove(v)
            adj[v].remove(u)
            cnt = 0
            visited = set()
            path = set()
            # print(adj)
            if dfs(1) and cnt == n:
                return [u,v]
            # print(cnt)
            adj[u].add(v)
            adj[v].add(u)
        
        return [3,3]
