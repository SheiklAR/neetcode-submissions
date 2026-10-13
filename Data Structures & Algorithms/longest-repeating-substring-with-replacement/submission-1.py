class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if k == 0:
            max_ = 1
            cur = 1

            for i in range(1, len(s)):
                if s[i-1] != s[i]:
                    cur = 0
                cur += 1
                max_ = max(cur, max_)
            
            return max_



        #if whatever the max no of char in the substring can 
        #fill up the remaining substring, that length is the answer
        #meaning freq(mostRepeatedChar) + k >= len(substring) then 
        #it is the answer because the whole substring would be
        #of one character otherwise i twon't
        #else: shrink the size of window by one by looking at the
        #boundary chars(choose which one is lesser of the two ends).
        #repeat.

        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

        l,r = 0, len(s) - 1
        
        while l < r:
            print(freq)
            length = r - l + 1
            big_char = max(freq, key=freq.get)
            print(big_char)
            print(length)
            if freq[big_char] + k >= length:
                return length

            if freq[s[l]] < freq[s[r]]:
                freq[l] -= 1
                l += 1
            else:
                freq[s[r]] -= 1
                r -= 1
            
            print('l', l, 'r', r)
