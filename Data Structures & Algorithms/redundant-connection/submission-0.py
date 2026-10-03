class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(0, len(edges) + 1)]

        def root(x):
            if parent[x] != x:
                parent[x] = root(parent[x])
            return parent[x]
            

        def union(u, v):
            root_u = root(u)
            root_v = root(v)

            if root_u == root_v:
                return False
            
            parent[root_u] = root_v
            return True


        for u,v in edges:
            if not union(u, v):
                return [u, v]