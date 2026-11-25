class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)
        dp = [-1] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            # print('i', s[i])
            word = s[i]
            
            res = False
            if word in dic:
                res = dp[i+1]
                dp[i] = res or res
            
            for j in range(i+1, len(s)):
                word = word + s[j]
                # print(word)
                if word in dic:
                    # print(word)
                    res = dp[j+1] or res
                    dp[i] = res
                    
                
            dp[i] = res

        # print(dp)
        return dp[0]
