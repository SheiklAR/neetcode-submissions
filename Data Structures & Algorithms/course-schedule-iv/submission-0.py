class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        isReachable = defaultdict(set)
        p = prerequisites

        for u,v in p:
            adj[u].add(v)
        


        def dfs(node, set_):

            for nei in adj[node]:
                set_.add(nei)
                dfs(nei, set_)
            
            return set_
            
        
        for n in range(numCourses):
            # set_ = set()

            isReachable[n] = dfs(n, set())
        
        ans = []
        # print(isReachable)
        

        for u,v in queries:
            if v in isReachable[u]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans