class Solution:
    def isMatch(self, s: str, p: str) -> bool:
            d = {}
        
            # "aaca"
            # p =
            # "ab*a*c*a"

            def dfs(i,j):
                key = (i, j)
                if key in d:
                    return d[key]
                    
                if i >= len(s) and j >= len(p):
                    return True
                
                if j >= len(p): return False

                # if i goes out of bound check we can skip them
                if i >= len(s):
                    cnt = p[j:].count('*')
                    return cnt * 2 == len(p[j:])
                
                res = False

                # dot
                if p[j] == '.':
                    # star combined
                    if j + 1 < len(p) and p[j+1] == '*':
                        res = res or dfs(i+1, j) or dfs(i+1, j+2) or dfs(i, j+2)
                    else:
                        #without star
                        res = res or dfs(i+1, j+1)

                # char
                # with star
                if j + 1 < len(p) and p[j+1] == '*':
                    # print(s[i])
                    if s[i] == p[j]:
                        res = res or dfs(i+1, j) or dfs(i, j+2)
                    else:
                        res = res or dfs(i, j+2)
                else:
                    # without star
                    if s[i] == p[j]:
                        res = res or dfs(i+1, j+1)
                    # else:
                    #     res = res or False
                
                d[key] = res
                return d[key]

            return dfs(0, 0)