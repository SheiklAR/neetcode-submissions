class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        parent = [i for i in range(n)]
        
        # n -> 0 - n - 1

        # undirected eges

        # 2 <- 0 -> 1 

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False
            
            parent[root_u] = parent[root_v]
            return True


        for u,v in edges:
            if not union(u, v):
                return False
        

        for i in range(n):
            find(i)
        
        for i in range(1, n):
            if parent[i-1] != parent[i]:
                return False
        

        return True



