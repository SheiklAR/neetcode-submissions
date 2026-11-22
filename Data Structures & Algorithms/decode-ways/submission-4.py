class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        # @cache
        def dfs(i):
            if i in dp:
                return dp[i]

            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0
            
            res1 = dfs(i+1)

            res2 = 0

            if i + 1 < len(s):
                if (
                    (s[i] == '1' and s[i + 1] in "0123456789") or
                    (s[i] == '2' and s[i+1] in "0123456")
                ):
                    res2 = dfs(i+2)
            
            dp[i] = res1 + res2
            return dp[i]


        return dfs(0)