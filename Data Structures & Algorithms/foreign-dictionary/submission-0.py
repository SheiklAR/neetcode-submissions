class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = defaultdict(list)
        chars = set()

        for i in range(len(words) - 1):
            l1, l2 = len(words[i]), len(words[i+1])
            if l1 > l2:
                return False
            if l2 > l1:
                continue
            
            chars.update(set(list(words[i])))
            chars.update(set(list(words[i+1])))

            j = 0
            while j < l1:
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].append(words[i+1][j])
                    break

                j += 1

        print(adj) 
        #  n < f
        def dfs(c, order):
            if c not in adj:
                return len(order) == cnt
            
            if c in visited:
                return False
            

            visited.add(c)
            cnt += 1

            for char in adj[c]:
                order.append(char)
                if dfs(char, order):
                    return order
                
                order.pop()
            
            return order
        


        for c in adj.keys():
            visited = set()
            x = dfs(c, [c])
            if len(x) == len(chars):
                return ''.join(x)



        return ''
