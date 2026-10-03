class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        
        def root(x):
            if parent[x] != x:
                parent[x] = root(parent[x])
            return parent[x]



        def union(u, v):
            root_u = root(u)
            root_v = root(v)

            if root_u == root_v:
                return

            parent[root_u] = root_v

        for u,v in edges:
            union(u, v)
        

        for i in range(n):
            parent[i] = root(i)
        
        c = Counter(parent)

        return len(c)
