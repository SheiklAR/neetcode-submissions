class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        # i, j = 0, 0
        N = len(s3)
        d = {}

        def dfs(i,j):
            key = (i,j)

            if key in d:
                return d[key]

            k = i + j

            if k >= N:
                return True
            
            res = False

            if i >= len(s1):
                res = s2[j:] == s3[k:]
            elif j >= len(s2):
                res = s1[i:] == s3[k:]

            elif s3[k] == s1[i] and s3[k] == s2[j]:
                res = dfs(i + 1, j) or dfs(i, j+1)
            
            elif s3[k] == s1[i]:
                res = dfs(i+1, j)
            elif s3[k] == s2[j]: 
                res = dfs(i, j+1)
            
            d[key] = res
            return d[key]
                

        return dfs(0, 0)