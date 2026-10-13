class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''

        def get_palindrome(i, j):
            if i < 0 or j >= len(s) or s[i] != s[j]: return s[i+1:j]
            

            #dad

            while i >= 0 or j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            
            return s[i+1:j]
        
    
        for i in range(len(s)):
            x = get_palindrome(i-1, i+1)
            if len(x) > len(ans):
                ans = x
            # ans = max(ans, x)

            if i+2 <= len(s):
                if s[i] == s[i+1]:
                    y = get_palindrome(i-1, i+2)
                    if len(y) > len(ans):
                        ans = y
                

        return ans