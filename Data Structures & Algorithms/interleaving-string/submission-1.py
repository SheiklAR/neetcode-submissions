class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # i, j = 0, 0
        N = len(s3)

        def dfs(i,j):
            k = i + j

            if k > N:
                return True
            
            if i >= len(s1):
                # k -= 1
                return s2[j:] == s3[k:]
            if j >= len(s2):
                # k -= 1
                return s1[i:] == s3[k:]

            

            if s3[k] == s1[i] and s3[k] == s2[j]:
                return dfs(i + 1, j) or dfs(i, j+1)
            
            if s3[k] == s1[i]:
                return dfs(i+1, j)
            elif s3[k] == s2[j]: 
                return dfs(i, j+1)
            else:
                return False

        return dfs(0, 0)