class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        d = {}

        i = 0
        ans = 0

        for j in range(len(s)):
            c = s[j]
            # print('c', c)
            if c in d:
                print(c)
                i = d[c] + 1
                print(i)
            d[c] = j
            print(d[c])
            # print(i,j)
            ans = max(ans, j-i+1)
        
        return ans
        

