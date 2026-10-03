class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b] -> 0 -> 1 -> 4 -> 8 
        adj = defaultdict(list)
        for v,u in prerequisites:
            adj[u].append(v)
        

        visit = set()
        path = set()

        def dfs(u):
            if u in path:
                return False
            

            if u in visit:
                return True

            path.add(u)
            for v in adj[u]:
                if not dfs(v):
                    return False

            path.remove(u)
            visit.add(u)
            return True
        

        
        for u in range(numCourses):
            if u not in visit and adj[u]:
                if not dfs(u):
                    return False
        
        return True