class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            return string == string[::-1]
        
        part = []
        res = []
        global n
        n = len(s)

        def bt(i):
            global n
            if i >= n:
                res.append(part[:])

            for j in range(i, n):
                substring = s[i:j+1]
                if isPalindrome(substring):
                    part.append(substring)
                    bt(j+1)
                    part.pop()
        
        bt(0)
        return res