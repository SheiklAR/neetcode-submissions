class Solution:
    def numDecodings(self, s: str) -> int:
        # if s[0] == '0':
        #     return 0
        n = len(s)

        cache = {}
        
        def dfs(index):
            if index >= n:
                return 1

            if s[index] == '0':
                return 0

            
            ways = dfs(index+1)

            if index + 1 < n and 1 <= int(s[index]+s[index+1]) <= 26 :
                ways += dfs(index+2)
            
            cache[index] = ways

            return ways


        return dfs(0)            
                
