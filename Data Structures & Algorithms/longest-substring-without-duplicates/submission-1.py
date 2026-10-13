class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)

        i = 0
        d[s[i]] = 1
        ans = 1

        for j in range(1,len(s)):
            if s[i] == 0:
                s[i] = j
            else:
                # d[s[j]] = d[s[j]]
                if d[s[j]] != 0:
                    i = d[s[j]] + 1
                
                d[s[j]] = j
            ans = max(ans, j-i+1)
        
        return ans
        

        return ans
        

