class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        ans = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[i])
                l += 1
            charSet.add(s[i])
            ans = max(ans, len(charSet))
        
        return ans

