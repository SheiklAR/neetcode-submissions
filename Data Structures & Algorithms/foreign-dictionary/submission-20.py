class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        
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
                continue
            chars.update(set(list(words[i])))
            chars.update(set(list(words[i+1])))
        # print('here')
        print(chars)
        print(adj) 

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
        
        
        # if not adj:
        #     return ''
        
        for src in chars:
            if src not in visited:
                if not dfs_post_order(src):
                    return ''
        
        
        print(post_order)
        return ''.join(reversed(post_order))



        #  n < f
        # def dfs(c, order):
        #     nonlocal ans
        #     if c not in adj:
        #         if len(ans) < len(order):
        #             ans = order[:]
        #         return order

            
        #     if c in visited:
        #         if len(ans) < len(order):
        #             ans = order[:]
        #         return order
            

        #     visited.add(c)
        #     # cnt += 1

        #     for char in adj[c]:
        #         order.append(char)
        #         y = dfs(char, order)
        #         if len(y) == len(chars):
        #             print('isnide here')
        #             print('here', y)
        #             return y
                
        #         x = order.pop()
        #         # visited.remove(x)
            
        #     return order
        

        # ans = []

        # for c in adj.keys():
        #     visited = set()
        #     x = dfs(c, [c])
        #     if len(x) == len(chars):
        #         return ''.join(x)
            
 
        
        # print('here')
        # if len(ans) == 0:
        #     return ''
        # print(ans)
        # print(chars)
        # tmp_list = []

        # for c in list(chars):
        #     if c not in ans:
        #         tmp_list.append(c)

        # print(tmp_list)
        # if len(tmp_list) + len(ans) < len(chars):
        #     print('here')
        #     return ''
        # else:
        #     str1 = ''.join(tmp_list)
        #     str2 = ''.join(ans)

        #     return str1 + str2

