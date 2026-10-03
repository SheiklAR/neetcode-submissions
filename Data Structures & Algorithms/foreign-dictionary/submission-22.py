from heapq import heappush, heappop

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return ''.join(list(set(list(words[0]))))
        
        adj = defaultdict(list)
        chars = set()

        for i in range(len(words) - 1):
            l1, l2 = len(words[i]), len(words[i+1])
            
            j = 0
            while j < l1 and j < l2:
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].append(words[i+1][j])
                    break

                j += 1

            if (j == l1 or j == l2) and l1 > l2:
                return ''
                # continue
            chars.update(set(list(words[i])))
            chars.update(set(list(words[i+1])))
        # print('here')


        post_order = []
        path = set()
        visited = set()

        def dfs_post_order(c):
            if c in path: # cycle detected, topological sort impossible
                return False

            if c in visited:
                return True
            
            path.add(c)
            for char in adj[c]:
                if not dfs_post_order(char):
                    return False
                
                
            visited.add(c)
            path.remove(c)
            post_order.append(c)
            return True
        

        # indegree
        indegree = defaultdict(int)

        for u in adj.keys():
            for v in adj[u]:
                indegree[v] += 1
        
        # visited = set()'
        heap = []
        ans = []
        for v in chars:
            if indegree[v] == 0:
                heappush(heap, v)

        print(indegree)
        # if len(heap) == 0:
        #     return ''
        
        while heap:
            u = heappop(heap)
            ans.append(u)

            for v in adj[u]:
                if v in visited:
                    return ''
                indegree[v] -= 1
                if indegree[v] == 0:
                    heappush(heap, v)
            
        
        return ''.join(ans) if len(chars) == len(ans) else ''