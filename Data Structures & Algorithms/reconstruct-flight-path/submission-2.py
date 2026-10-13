class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for u,v in tickets:
            adj[u].append(v)

        
        for key in adj.keys():
            adj[key] = deque(sorted(adj[key]))

        ans = []

        def dfs(node):

            ans.append(node)

            if adj[node]:
                nei = adj[node][0]
                adj[node].popleft()
                dfs(nei)
        

        dfs("JFK")
        return ans
        