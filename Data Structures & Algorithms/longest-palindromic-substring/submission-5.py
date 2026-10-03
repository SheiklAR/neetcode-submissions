class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]

        def get_palindrome(i, j):
            if i < 0 or j >= len(s) or s[i] != s[j]:
                return s[i+1:j]
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            
            return s[i+1:j]
        

    
        for i in range(len(s)):
            res1 = get_palindrome(i-1, i+1)
            if len(res1) > len(ans):
                ans = res1

            if i+1 < len(s) and s[i] == s[i+1]:
                res2 = get_palindrome(i-1, i+2)
                if len(res2) > len(ans):
                    ans = res2

        return ans
