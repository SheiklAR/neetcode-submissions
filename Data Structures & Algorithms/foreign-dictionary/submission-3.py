class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = defaultdict(list)
        chars = set()

        for i in range(len(words) - 1):
            l1, l2 = len(words[i]), len(words[i+1])
            # if l1 > l2:
            #     continue
            # if l2 > l1:
            #     continue
            
            chars.update(set(list(words[i])))
            chars.update(set(list(words[i+1])))

            j = 0
            while j < l1 and j < l2:
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].append(words[i+1][j])
                    break

                j += 1

        print('here')
        print(adj) 
        #  n < f
        def dfs(c, order):
            if c not in adj:
                return order
            
            if c in visited:
                return []
            

            visited.add(c)
            # cnt += 1

            for char in adj[c]:
                order.append(char)
                if len(dfs(char, order)) == len(chars):
                    return order
                
                order.pop()
            
            return order
        

        ans = ['']

        for c in adj.keys():
            visited = set()
            x = dfs(c, [c])
            if len(x) == len(chars):
                return ''.join(x)
            
            if len(x) > len(ans):
                ans = x
        
        tmp_list = []

        for c in ans:
            if c not in visited:
                tmp_list.append(c)


        if len(tmp_list) + len(ans) < len(visited):
            return ''
        else:
            str1 = ''.join(tmp_list)
            str2 = ''.join(ans)

            return str1 + str2

