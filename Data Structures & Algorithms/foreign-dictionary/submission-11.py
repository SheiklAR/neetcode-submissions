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

        # print('here')
        print(chars)
        print(adj) 
        #  n < f
        def dfs(c, order):
            nonlocal ans
            if c not in adj:
                if len(ans) < len(order):
                    ans = order[:]
                return order

            
            if c in visited:
                if len(ans) < len(order):
                    ans = order[:]
                return order
            

            visited.add(c)
            # cnt += 1

            for char in adj[c]:
                order.append(char)
                if len(dfs(char, order)) == len(chars):
                    return order
                
                order.pop()
            
            return order
        

        ans = []

        for c in adj.keys():
            visited = set()
            x = dfs(c, [c])
            if len(x) == len(chars):
                return ''.join(x)
            
 
        
        print('here')
        if len(ans) == 0:
            return ''
        print(ans)
        print(chars)
        tmp_list = []

        for c in list(chars):
            if c not in ans:
                tmp_list.append(c)

        print(tmp_list)
        if len(tmp_list) + len(ans) < len(chars):
            print('here')
            return ''
        else:
            str1 = ''.join(tmp_list)
            str2 = ''.join(ans)

            return str1 + str2

