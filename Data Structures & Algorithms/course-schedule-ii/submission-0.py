class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for v,u in prerequisites:
            adj[u].append(v)
        
        ans = []
        path = set()
        visited = set()
        ans_set = set()


        def dfs(u):
            if u in path:
                return False
            
            if u in visited:
                return True
            
            path.add(u)
            for v in adj[u]:
                if not dfs(v):
                    return False
                else:
                    if v not in ans_set:
                        ans.append(v)
                        ans_set.add(v)
                
        
            path.remove(u)
            visited.add(u)
            return True


        for u in range(numCourses):
            if u not in visited:
                if adj[u]:
                    if not dfs(u):
                        return []
                ans.append(u)
                ans_set.add(u)
        
        ans.reverse()
        return ans