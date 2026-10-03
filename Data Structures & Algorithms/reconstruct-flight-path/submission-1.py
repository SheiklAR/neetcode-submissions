from heapq import heappop, heappush

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        # tickets.sort()
        for u,v in tickets:
            heappush(adj[u], v)
            # adj[u].append(v)
            

        # for key in adj.keys():
        #     adj[key].sort()
        

        ans = []
        
        def dfs(s):
            while adj[s]:
                x = heappop(adj[s])
                dfs(x)
            ans.append(s)
            
            
        dfs("JFK")
        return ans[::-1]
        # adj = defaultdict(list)

        # # starts = set()

        # for u,v in tickets:
        #     adj[u].append(v)
        #     # starts.add(u)


        # for key in adj.keys():
        #     adj[key].sort()

        # ans = ["JFK"]

        
        # def dfs(s):

        #     if len(tickets) + 1 == len(ans):
        #         return True
        #     if s not in adj:
        #         return False

        #     temp = adj[s]
        #     for i, v in enumerate(temp):
        #         adj[s].pop(i)
        #         ans.append(v)
        #         if dfs(v): return True

        #         ans.pop()
        #         adj[s].insert(i, v)
            
        #     return False
        
        # dfs("JFK")
        # return ans