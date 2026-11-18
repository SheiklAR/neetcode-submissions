class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        def count_palindrome(left, right):
            nonlocal cnt

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                        # print(s[right])
                        cnt += 1
                else:
                    break

                left -= 1
                right += 1
        
        for i in range(len(s)):
            count_palindrome(i, i)
            count_palindrome(i, i+1)
        
        return cnt