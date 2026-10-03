class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        #map chars
        chars = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        #convert digits to arr or leave it
        ans = []
        global n
        n = len(digits)
        #bt {}
        def bt(i, s):
            global n
            if i >= n:
                ans.append(s)
                return

            #for loop for every num
            digit = int(digits[i])
            for char in chars[digit]:
                #for each iteration add chars to s
                s += char
                bt(i+1, s)
                s = s[:-1]

                #if s == len(digits) add it to the ans and return
                #pop the last char or not this is just a string

        
        bt(0, '')
        return ans